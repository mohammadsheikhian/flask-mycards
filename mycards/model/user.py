# from ..principal import JWTPrincipal
from . import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    title = db.Column(
        db.String(100),
    )
    first_name = db.Column(
        db.String(100),
        nullable=True,
    )
    last_name = db.Column(
        db.String(100),
        nullable=True,
    )
    cards = db.relationship(
        'Card',
        back_populates='user',
        lazy=True,
    )

    def __init__(self, title, first_name=None, last_name=None):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        result = dict(
            id=self.id,
            title=self.title,
            firstName=self.first_name,
            lastName=self.last_name,
        )
        return result

    # def create_jwt_principal(self):
    #     return JWTPrincipal(self.to_dict())

