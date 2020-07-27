from flask import *

from tests.helpers import BaseTestCase


class TestUser(BaseTestCase):

    def test_post(self):
        title = 'mohammad'
        form = dict(
            title=title,
        )
        response = self.client.post(
            '/users',
            data=form,
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        resp = json.loads(response.json)
        self.assertEqual(resp['title'], title)
