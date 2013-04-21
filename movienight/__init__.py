from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('movienight.config')
db = SQLAlchemy(app)

from movienight import views, models, admin
