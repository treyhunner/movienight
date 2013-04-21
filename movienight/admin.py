from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView

from movienight import db, app, models

admin = Admin(app)

admin.add_view(ModelView(models.Person, db.session, endpoint='person'))
admin.add_view(ModelView(models.Event, db.session, endpoint='event'))
