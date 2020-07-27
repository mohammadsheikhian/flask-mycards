from flask import *

from mycards import db
from mycards.model import Card
from tests.helpers import BaseTestCase


class TestCard(BaseTestCase):

    def test_get(self):
        card = Card(
            title='mohammad',
            cvv2='1234',
        )
        db.session.add(card)
        db.session.commit()

        response = self.client.open(f'/cards/{card.id}', method='get')
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        resp = json.loads(response.json)
        self.assertEqual(resp['title'], card.title)
        self.assertEqual(resp['cvv2'], card.cvv2)

        # Not found card
        response = self.client.open('/cards/0', method='get')
        self.assert_status(response, 404)
