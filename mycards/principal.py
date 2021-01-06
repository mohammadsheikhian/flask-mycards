from itsdangerous import TimedJSONWebSignatureSerializer, \
    JSONWebSignatureSerializer

from .app import get_app


class JWTPrincipal:
    def __init__(self, payload):
        self.payload = payload

    @classmethod
    def create_serializer(cls, force=False, max_age=None):
        secret = get_app().config.get('SECRET_KEY')
        algorithm = get_app().config.get('AUTHORIZATION_ALGORITHM')
        if max_age is None:
            max_age = get_app().config.get('AUTHORIZATION_MAX_AGE')

        if force:
            return JSONWebSignatureSerializer(
                secret,
                algorithm_name=algorithm
            )
        else:
            return TimedJSONWebSignatureSerializer(
                secret,
                expires_in=max_age,
                algorithm_name=algorithm
            )

    def dump(self, max_age=None):
        return self.create_serializer(max_age=max_age).dumps(self.payload)

    @classmethod
    def load(cls, encoded, force=False):
        if encoded.startswith('Bearer '):
            encoded = encoded[7:]
        payload = cls.create_serializer(force=force).loads(encoded)
        return cls(payload)

