from movienight import db


attendance = db.Table('attendance', db.Model.metadata,
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)
    picks = db.relationship('Event', backref='picker', lazy='dynamic')

    def __repr__(self):
        return "<Person %r>" % self.name


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    movie = db.Column(db.String(50))
    picker_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    attendees = db.relationship('Person', secondary=attendance,
                                backref=db.backref('events', lazy='dynamic'))

    def __repr__(self):
        return "<Event %r>" % self.movie
