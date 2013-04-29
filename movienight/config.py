import os

base = os.path.abspath(os.path.dirname(__file__))

default_database_url = "sqlite:///{0}/movienight.db".format(base)

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default_database_url)
SECRET_KEY = "\xccK\xd6V-L\xe1\xeeR:\x84\x05y\xcb)\xb0\x9c\x86\x9bWRE%\xf4"
