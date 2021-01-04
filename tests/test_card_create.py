from flask import *

from mycards import db
from mycards.model import User
from mycards.principal import JWTPrincipal
from tests.helpers import BaseTestCase


class TestCard(BaseTestCase):

    def test_create(self):
        user1 = User(
            title='mohammad',
        )
        db.session.add(user1)
        db.session.commit()

        jwt_principal = JWTPrincipal(dict(id=user1.id))
        token = jwt_principal.dump()

        title = 'mohammad'
        cvv2 = '1234'
        form = dict(
            title=title,
            cvv2=cvv2,
        )
        response = self.client.open(
            path='/cards',
            method='create',
            data=form,
            headers=dict(
                authorization=token,
            )
        )
        self.assert_status(response, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        resp = json.loads(response.json)
        self.assertEqual(resp['title'], title)
