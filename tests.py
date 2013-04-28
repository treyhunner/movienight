#!/usr/bin/env python
from datetime import date
import unittest
from webtest import TestApp

from movienight.config import base
from movienight import app, db
from movienight.models import Person, Event


class AdminTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{0}/test.db".format(base)
        self.app = TestApp(app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_people(self):
        people = [
            Person(name="David"),
            Person(name="Claudia"),
            Person(name="Cesar"),
            Person(name="Tricia"),
        ]
        for person in people:
            db.session.add(person)
        db.session.commit()
        return people

    def create_events(self):
        people = self.create_people()
        events = [
            Event(movie="The Matrix", date=date(2013, 4, 1), picker=people[0]),
            Event(movie="Fight Club", date=date(2013, 4, 8), picker=people[1]),
            Event(movie="Psycho", date=date(2013, 4, 15), picker=people[2]),
            Event(movie="Alien", date=date(2013, 4, 22), picker=people[0]),
            Event(movie="Yojimbo", date=date(2013, 4, 29), picker=people[1]),
            Event(movie="Goodfellas", date=date(2013, 5, 6), picker=people[2]),
            Event(movie="Toy Story", date=date(2013, 5, 13), picker=people[0]),
        ]
        for event in events:
            event.attendees = people[:3]
        db.session.commit()
        return events

    def test_create_event(self):
        self.create_people()
        home = self.app.get('/admin/')
        event_list = home.click("Event")
        create_event = event_list.click("Create")
        people_ids = [p.id for p in Person.query.all()]
        create_event.form['attendees'] = people_ids
        create_event.form['date'].value = "2013-04-01"
        create_event.form['movie'].value = "Leon"
        create_event.form['picker'] = people_ids[0]
        create_event.form.submit()
        events = Event.query.all()
        self.assertEqual(len(events), 1)
        self.assertItemsEqual([p.id for p in events[0].attendees], people_ids)
        self.assertEqual(unicode(events[0].date), '2013-04-01')
        self.assertEqual(events[0].movie, "Leon")
        self.assertEqual(events[0].picker.id, people_ids[0])

    def test_create_person(self):
        home = self.app.get('/admin/')
        people_list = home.click("Person")
        create_person = people_list.click("Create")
        create_person.form['name'].value = "Janelle"
        create_person.form.submit()
        people = Person.query.all()
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0].name, "Janelle")

    def test_event_list(self):
        self.create_events()
        home = self.app.get('/admin/')
        event_list = home.click("Event")
        self.assertIn("The Matrix", event_list)
        self.assertIn("2013-04-01", event_list)
        self.assertIn("Fight Club", event_list)
        self.assertIn("2013-04-08", event_list)

    def test_person_list(self):
        self.create_events()
        home = self.app.get('/admin/')
        people_list = home.click("Person")
        self.assertIn("David", people_list)
        self.assertIn("Claudia", people_list)
        self.assertIn("Cesar", people_list)
        self.assertIn("Tricia", people_list)
        self.assertIn("Toy Story, Alien, The Matrix", people_list)
        self.assertIn("Yojimbo, Fight Club", people_list)
        self.assertIn("Goodfellas, Psycho", people_list)
        self.assertIn("33", people_list)
        self.assertIn("-67", people_list)
        self.assertIn("N/A", people_list)


if __name__ == '__main__':
    unittest.main()
