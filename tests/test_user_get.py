from flask import *

from mycards import db
from mycards.model import User
from tests.helpers import BaseTestCase


class TestUser(BaseTestCase):

    def test_get(self):
        user = User(
            title='mohammad',
        )
        db.session.add(user)
        db.session.commit()

        response = self.client.open(f'/users/{user.id}', method='get')
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], user.title)

        # Not found card
        response = self.client.open('/users/0', method='get')
        self.assert_status(response, 404)
