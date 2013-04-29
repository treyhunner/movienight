import os

base = os.path.abspath(os.path.dirname(__file__))

default_database_url = "sqlite:///{0}/movienight.db".format(base)
default_secret = "\xccK\xd6V-L\xe1\xeeR:\x84\x05y\xcb)\xb0\x9c\x86\x9bWRE%\xf4"

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default_database_url)
SECRET_KEY = os.environ.get('SECRET_KEY', default_secret)
