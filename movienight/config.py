import os

base = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/movienight.db".format(base)
SECRET_KEY = "\xccK\xd6V-L\xe1\xeeR:\x84\x05y\xcb)\xb0\x9c\x86\x9bWRE%\xf4"
