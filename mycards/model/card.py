from . import db


class Card(db.Model):
    id = db.Column(
        'employee_id',
        db.Integer,
        primary_key=True,
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )
    title = db.Column(
        db.String(100),
    )
    cvv2 = db.Column(
        db.Float(50),
    )
    user = db.relationship(
        'User',
        back_populates='cards',
        lazy=True,
    )

    def to_dict(self):
        result = dict(
            id=self.id,
            title=self.title,
            cvv2=self.cvv2,
            user_id=self.user_id,
        )
        return result
