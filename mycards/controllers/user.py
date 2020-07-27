from flask import *
from mycards.utill import json as json_decorate
from mycards.model import db, User


user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/users', methods=['post'])
@json_decorate
def post():
    title = request.form.get('title')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    user = User(
        title=title,
        first_name=first_name,
        last_name=last_name,
    )
    db.session.add(user)
    db.session.commit()
    return user.to_dict()


@user_blueprint.route('/users/<int:user_id>', methods=['get'])
@json_decorate
def get(user_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        abort(404)
    return user.to_dict()


@user_blueprint.route('/users/<int:user_id>', methods=['put'])
@json_decorate
def put(user_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        abort(404)

    title = request.json.get('title')
    user.title = title if title is not None else user.title

    db.session.commit()
    return user.to_dict()
