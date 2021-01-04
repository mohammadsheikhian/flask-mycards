from flask import *

from mycards import db
from mycards.model import User
from tests.helpers import BaseTestCase
from mycards.principal import JWTPrincipal


class TestUser(BaseTestCase):

    def test_get(self):
        user = User(
            title='mohammad',
        )
        db.session.add(user)
        db.session.commit()
        jwt_principal = JWTPrincipal(dict(id=user.id))
        token = jwt_principal.dump()

        response = self.client.get(
            f'/users/{user.id}',
            method='get',
            headers=dict(
                authorization=token,
            ),
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], user.title)

        # Not found card
        response = self.client.open(
            '/users/0',
            method='get',
            headers=dict(
                authorization=token,
            ),
        )
        self.assert_status(response, 404)
