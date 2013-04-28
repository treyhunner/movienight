from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView

from movienight import db, app, models


class PersonView(ModelView):
    column_list = ('name', 'recent_picks', 'score')


class EventView(ModelView):
    column_list = ('date', 'movie', 'picker', 'attendees')
    column_sortable_list = ('date', 'movie', ('picker', models.Person.name))
    column_searchable_list = ('movie',)
    column_filters = ('picker',)


admin = Admin(app, name="Movie Night")


admin.add_view(PersonView(models.Person, db.session, endpoint='person'))
admin.add_view(EventView(models.Event, db.session, endpoint='event'))
