Movie Night Turn Tracker
========================

This repository will contain code for a website that will track who should
pick next for movie night.

Usage
-----

Before you can run the website you will need to install the dependencies:

.. code-block:: bash

    $ pip install -r requirements.txt

Once you have the required dependencies you should create the database file:

.. code-block:: bash

    $ ./create_db.py

Now you can run the website (on port 5000 by default):

.. code-block:: bash

    $ ./runserver.py

Tools
-----

- `Flask`_
- `SQLAlchemy`_ (with `Flask-SQLAlchemy`_)
- `Flask-Admin`_

Runinng Tests
-------------

Run the tests by executing the ``tests.py`` file:

.. code-block:: bash

    $ ./tests.py

To run an individual test use this format:

.. code-block:: bash

    $ python -m unittest tests.AdminTest.test_create_event

.. _Flask: http://flask.pocoo.org/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Flask-SQLAlchemy: http://pythonhosted.org/Flask-SQLAlchemy/
.. _Flask-Admin: https://flask-admin.readthedocs.org/en/latest/
