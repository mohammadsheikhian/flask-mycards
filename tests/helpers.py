from flask_testing import TestCase
from flask import *

from mycards import app, db


class BaseTestCase(TestCase):

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db-testing.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    SECRET_KEY = 'test-secret-key'

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        app.config['SECRET_KEY'] = self.SECRET_KEY
        app.config['TESTING'] = self.TESTING
        return app

    def setUp(self):
        db.create_all(app=app)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
