from . import db


class Card(db.Model):
    id = db.Column(
        'employee_id',
        db.Integer,
        primary_key=True,
    )
    title = db.Column(
        db.String(100),
    )
    cvv2 = db.Column(
        db.Float(50),
    )

    def __init__(self, title, cvv2):
        self.title = title
        self.cvv2 = cvv2

    def to_dict(self):
        result = dict(
            id=self.id,
            title=self.title,
            cvv2=self.cvv2,
        )
        return result
