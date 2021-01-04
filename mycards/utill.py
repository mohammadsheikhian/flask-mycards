from functools import wraps

import jwt
from flask import jsonify, json, request, abort

from .model import db


def to_json(func):
    """
    https://stackoverflow.com/questions/21352718/python-decorator-with-flask
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return jsonify(json.dumps(result))
    return wrapper


def authorize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        authorization_token = request.headers.get('authorization')
        if authorization_token is None:
            abort(401)

        from . import app
        key = app.config.get('SECRET_KEY')
        try:
            from .principal import JWTPrincipal
            identify = JWTPrincipal.load(authorization_token)
            request.identity = identify

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
