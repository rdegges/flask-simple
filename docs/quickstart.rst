.. _quickstart:
.. module:: flask.ext.simple


Quickstart
==========

This section will guide you through everything you need to know to get up and
running with flask-simple!


Installation
------------

The first thing you need to do is install flask-simple.  Installation can be
done through `pip`_, the Python package manager.

To install flask-simple, run::

    $ pip install flask-simple

If you'd like to upgrade an existing installation of flask-simple to the latest
release, you can run::

    $ pip install -U flask-simple


Set Environment Variables
-------------------------

In order to run properly, flask-simple requires that you set several environment
variables.

The required environment variables are:

- ``AWS_ACCESS_KEY_ID`` (*your Amazon access key ID*)
- ``AWS_SECRET_ACCESS_KEY`` (*your Amazon secret access key*)

There is also an optional variable you can set:

- ``AWS_REGION`` (*defaults to us-east-1*)

These credentials can be grabbed from your `AWS Console`_.

.. note::
    A full list of Amazon regions can be found here:
    http://docs.aws.amazon.com/general/latest/gr/rande.html#sdb_region

If you're unsure of how to set environment variables, I recommend you check out
this `StackOverflow question`_.


Specify Your Domains
--------------------

The next thing you need to do is tell flask-simple which domains you'll be using.

If you're not sure how domains work with SimpleDB, you should read through the
`boto SimpleDB tutorial`_ before continuing.

The way you can specify your domains is by creating an array called
``SIMPLE_DOMAINS`` (*this is what flask-simple uses to set everything up*).

Below is an example::

    # app.py


    from flask import Flask
    from flask.ext.simple import Simple

    app = Flask(__name__)
    app.config['SIMPLE_DOMAINS'] = [
        'users',
        'groups',
    ]

In the above example, I'm defining two SimpleDB domains: ``users`` and
``groups``.

flask-simple will respect *any* boto domains you define.


Initialize simple
-----------------

Now that you've defined your domains, you can initialize flask-simple in your
app.

All you need to do is pass your app to the ``simple`` constructor::

    # app.py


    from flask import Flask
    from flask.ext.simple import Simple

    app = Flask(__name__)
    app.config['SIMPLE_DOMAINS'] = [
        'users',
        'groups',
    ]

    simple = Simple(app)

From this point on, you can interact with SimpleDB through the global ``simple``
object.


Create Your Domains
-------------------

If you haven't already created your SimpleDB domains, flask-simple can help you
out!

After configuring flask-simple, you can use the following code snippet to create
all of your predefined SimpleDB domains::

    with app.app_context():
        simple.create_all()

This works great in bootstrap scripts.


Working with Domains
--------------------

Now that you've got everything setup, you can easily access your domains in one
of two ways: you can either access the domains directly from the ``simple``
global, or you can access the domains in a dictionary-like format through
``simple.domains``.

Below is an example view which creates a new user account::

    # app.py

    @app.route('/create_user')
    def create_user():
        simple.users.put_attributes('r@rdegges.com', {
            'username': 'rdegges',
            'first_name': 'Randall',
            'last_name': 'Degges',
            'email': 'r@rdegges.com',
        })

        # or ...

        simple.domains['users'].put_attributes('r@rdegges.com', {
            'username': 'rdegges',
            'first_name': 'Randall',
            'last_name': 'Degges',
            'email': 'r@rdegges.com',
        })

Either of the above will work the same.

.. note::
    When storing items in SimpleDB, you need to specify two fields: an item name
    (*the first parameter*), and the item contents (*a Python dictionary*).

On a related note, you can also use the ``simple.domains`` dictionary to
iterate through all of your domains (*this is sometimes useful*).  Here's how
you could iterate over your existing SimpleDB domains::

    # app.py

    with app.app_context():
        for domain_name, domain in simple.domains.iteritems():
            print domain_name, domain


Deleting Domains
----------------

If, for some reason, you'd like to destroy all of your predefined SimpleDB
domains, flask-simple can also help you with that.

The below code snippet will destroy all of your predefined SimpleDB domains::

    # app.py

    with app.app_context():
        simple.destroy_all()

.. note::
    Please be *extremely* careful when running this -- it has the potential to
    completely destroy your application's data!


.. _pip: http://pip.readthedocs.org/en/latest/
.. _AWS Console: https://console.aws.amazon.com/iam/home?#security_credential
.. _StackOverflow question: http://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
.. _boto SimpleDB tutorial: http://boto.readthedocs.org/en/latest/simpledb_tut.html
