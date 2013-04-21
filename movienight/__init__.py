from flask import Flask

app = Flask(__name__)

from movienight import views
