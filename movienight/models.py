from __future__ import division

from movienight import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)
    picks = db.relationship('Event', backref='picker', lazy='dynamic')

    @property
    def recent_picks(self):
        return [unicode(pick) for pick in self.picks.order_by('-date')[:3]]

    @property
    def score(self):
        event_ids = [e.id for e in self.events]
        events = (db.session.query(Attendance.event_id, db.func.count())
                     .group_by(Attendance.event_id).all())
        score = sum(1 / count for id_, count in events if id_ in event_ids)
        score -= self.picks.count()
        return int(round(score * 100))

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return "<Person %r>" % self.name


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    movie = db.Column(db.String(50))
    picker_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    attendees = db.relationship('Person', secondary='attendance',
                                backref=db.backref('events', lazy='dynamic'))

    def __unicode__(self):
        return self.movie

    def __repr__(self):
        return "<Event %r>" % self.movie


class Attendance(db.Model):
    __tablename__ = 'attendance'
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    person = db.relationship('Person')
    event = db.relationship('Event')
    __table_args__ = (db.PrimaryKeyConstraint(person_id, event_id),)
