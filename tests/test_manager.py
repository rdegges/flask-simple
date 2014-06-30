"""Tests for our manager."""


from os import environ
from time import sleep
from unittest import TestCase
from uuid import uuid4

from boto.sdb.connection import SDBConnection
from boto.sdb.domain import Domain
from flask import Flask
from flask.ext.simple import Simple


class SimpleTest(TestCase):
    """Test our Simple extension."""

    def setUp(self):
        """
        Set up a simple Flask app for testing.

        This will be used throughout our tests.
        """
        self.prefix = uuid4().hex

        self.app = Flask(__name__)
        self.app.config['DEBUG'] = True
        self.app.config['SIMPLE_DOMAINS'] = [
            '%s-phones' % self.prefix,
            '%s-users' % self.prefix,
        ]

        self.simple = Simple(self.app)

        with self.app.app_context():
            self.simple.create_all()
            sleep(60)

    def test_settings(self):
        self.assertEqual(len(self.app.config['SIMPLE_DOMAINS']), 2)
        self.assertEqual(self.app.config['AWS_ACCESS_KEY_ID'], environ.get('AWS_ACCESS_KEY_ID'))
        self.assertEqual(self.app.config['AWS_SECRET_ACCESS_KEY'], environ.get('AWS_SECRET_ACCESS_KEY'))
        self.assertEqual(self.app.config['AWS_REGION'], environ.get('AWS_REGION') or self.simple.DEFAULT_REGION)

    def test_connection(self):
        with self.app.app_context():
            self.assertIsInstance(self.simple.connection, SDBConnection)

    def test_domains(self):
        with self.app.app_context():
            self.assertEqual(len(self.simple.domains.keys()), 2)

            for domain_name, domain in self.simple.domains.iteritems():
                self.assertIsInstance(domain, Domain)
                self.assertEqual(domain.name, domain_name)

    def test_domain_access(self):
        with self.app.app_context():
            for domain_name, domain in self.simple.domains.iteritems():
                self.assertEqual(getattr(self.simple, domain_name), domain)

    def tearDown(self):
        """Destroy all provisioned resources."""
        with self.app.app_context():
            self.simple.destroy_all()
            sleep(60)
