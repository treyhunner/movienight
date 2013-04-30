from flask.ext.admin import Admin
from flask.ext.admin.base import expose, AdminIndexView
from flask.ext.admin.contrib.sqlamodel import ModelView

from movienight import db, app, models


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        recent_events = models.Event.query.order_by('date desc')[:10]
        recent_attendees = models.Person.query.filter(models.Person.events.any(models.Event.id.in_(
            [e.id for e in recent_events]))).all()
        people = sorted(recent_attendees, key=lambda p: p.score, reverse=True)
        return self.render('index.html', people=people, events=recent_events)


class PersonView(ModelView):
    column_list = ('name', 'recent_picks', 'score')


class EventView(ModelView):
    column_list = ('date', 'movie', 'picker', 'attendees')
    column_sortable_list = ('date', 'movie', ('picker', models.Person.name))
    column_searchable_list = ('movie',)
    column_filters = ('picker',)


admin = Admin(app, name="Movie Night", index_view=MyHomeView())


admin.add_view(PersonView(models.Person, db.session, endpoint='person'))
admin.add_view(EventView(models.Event, db.session, endpoint='event'))
