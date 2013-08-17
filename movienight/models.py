from __future__ import division

from movienight import db

attendance = db.Table('attendance', db.Model.metadata,
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)
    picks = db.relationship('Event', backref='picker', lazy='dynamic')

    @property
    def recent_picks(self):
        return [unicode(pick) for pick in self.picks.order_by('date desc')[:3]]

    @property
    def score(self):
        score = int(round((sum(1 / len(e.attendees) for e in self.events)
            - len(self.picks.all())) * 100))
        if self.picks.count() == 0 and score < 75:
            score = 'N/A'
        return score

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return "<Person %r>" % self.name


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    movie = db.Column(db.String(50))
    picker_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    attendees = db.relationship('Person', secondary=attendance,
                                backref=db.backref('events', lazy='dynamic'))

    def __unicode__(self):
        return self.movie

    def __repr__(self):
        return "<Event %r>" % self.movie
