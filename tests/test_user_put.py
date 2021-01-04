from flask import *

from mycards import db
from mycards.model import User
from mycards.principal import JWTPrincipal
from tests.helpers import BaseTestCase


class TestUser(BaseTestCase):

    def test_put(self):
        user = User(
            title='mohammad',
        )
        db.session.add(user)
        db.session.commit()

        jwt_principal = JWTPrincipal(dict(id=user.id))
        token = jwt_principal.dump()

        new_title = 'ali'
        response = self.client.open(
            path=f'/users/{user.id}',
            method='put',
            json=dict(title=new_title),
            headers=dict(
                authorization=token,
            ),
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], new_title)

        # Not found card
        response = self.client.open(
            '/users/0',
            method='put',
            headers=dict(
                authorization=token,
            ),
        )
        self.assert_status(response, 404)
