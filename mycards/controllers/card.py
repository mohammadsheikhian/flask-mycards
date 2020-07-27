from flask import *
from mycards.utill import json as json_decorate, authorize
from mycards.model import db, Card


card_blueprint = Blueprint('card_blueprint', __name__)


@card_blueprint.route('/cards', methods=['create'])
@authorize
@json_decorate
def create():
    title = request.form.get('title')
    card = Card(
        title=title,
        cvv2='1234',
    )
    db.session.add(card)
    db.session.commit()
    return card.to_dict()


@card_blueprint.route('/cards/<int:card_id>', methods=['get'])
@json_decorate
def get(card_id):
    card = db.session.query(Card).get(card_id)
    if card is None:
        abort(404)
    return card.to_dict()


@card_blueprint.route('/cards/<int:card_id>', methods=['update'])
@json_decorate
def update(card_id):
    card = db.session.query(Card).get(card_id)
    if card is None:
        abort(404)

    title = request.json.get('title')
    card.title = title if title is not None else card.title

    cvv2 = request.json.get('cvv2')
    card.cvv2 = cvv2 if cvv2 is not None else card.cvv2

    db.session.commit()
    return card.to_dict()
