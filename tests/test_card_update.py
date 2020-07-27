from flask import *

from mycards import db
from mycards.model import Card
from tests.helpers import BaseTestCase


class TestCard(BaseTestCase):

    def test_update(self):
        card = Card(
            title='mohammad',
            cvv2='1234',
        )
        db.session.add(card)
        db.session.commit()

        new_title = 'ali'
        response = self.client.open(
            path=f'/cards/{card.id}',
            method='update',
            json=dict(title=new_title),
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], new_title)
        self.assertEqual(resp['cvv2'], card.cvv2)

        # Not found card
        response = self.client.open('/cards/0', method='update')
        self.assert_status(response, 404)
