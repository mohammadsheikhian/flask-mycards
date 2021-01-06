from flask import *

from mycards.model import Card, User, db
from mycards.principal import JWTPrincipal
from tests.helpers import BaseTestCase


class TestCard(BaseTestCase):

    def test_update(self):
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

        new_title = 'ali'
        response = self.client.open(
            path=f'/cards/{card.id}',
            method='update',
            json=dict(title=new_title),
            headers=dict(
                authorization=token,
            ),
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], new_title)
        self.assertEqual(resp['cvv2'], card.cvv2)

        # Not found card
        response = self.client.open(
            '/cards/0',
            method='update',
            headers=dict(
                authorization=token,
            ),
        )
        self.assert_status(response, 404)
