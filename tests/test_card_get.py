from flask import *

from mycards import db
from mycards.model import Card, User
from mycards.principal import JWTPrincipal
from tests.helpers import BaseTestCase


class TestCard(BaseTestCase):

    def test_get(self):
        user1 = User(
            title='mohammad',
        )

        card = Card(
            title='mohammad',
            cvv2='1234',
            user=user1,
        )
        db.session.add(card)
        db.session.commit()
        jwt_principal = JWTPrincipal(dict(id=user1.id))
        token = jwt_principal.dump()
        response = self.client.open(
            f'/cards/{card.id}',
            method='get',
            headers=dict(authorization=token.decode())
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], card.title)
        self.assertEqual(resp['cvv2'], card.cvv2)

        # Not found card
        response = self.client.open(
            '/cards/0',
            method='get',
            headers=dict(authorization=token.decode()),
        )
        self.assert_status(response, 404)

        # Unauthorized
        response = self.client.open(
            f'/cards/{card.id}',
            method='get',
        )
        self.assert_status(response, 401)

