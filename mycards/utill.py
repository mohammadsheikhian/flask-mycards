from functools import wraps

from flask import jsonify, json as j, request, abort
import jwt

from .model import db
from .controllers.card import app


def json(func):
    """
    https://stackoverflow.com/questions/21352718/python-decorator-with-flask
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return jsonify(j.dumps(result))
    return wrapper


def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        authorization_token = request.headers.get('authorization')
        if authorization_token is None:
            abort(401)

        key = app.config.get('SECRET_KEY')
        try:
            identify = jwt.decode(
                authorization_token,
                key=app.config.get('SECRET_KEY'),
            )
            app.identity = identify

        except jwt.ExpiredSignatureError:
            # 'Signature expired. Please log in again.'
            abort(401)

        except jwt.InvalidTokenError:
            # 'Invalid token. Please log in again.'
            abort(401)

        return func(*args, **kwargs)
    return wrapper


def commit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        db.session.commit()
        return result
    return wrapper
