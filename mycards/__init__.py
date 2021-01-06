from flask import Flask

from mycards.controllers.user import user_blueprint
from mycards.controllers.card import card_blueprint


app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(card_blueprint)
app.__version__ = '0.1.0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret key'
app.config['AUTHORIZATION_ALGORITHM'] = 'HS256'
app.config['AUTHORIZATION_MAX_AGE'] = 86400  # 24 Hours


def init_db():
    from mycards.model import db
    db.init_app(app)
    return db


init_db()


@app.route('/version')
def version():
    return app.__version__


if __name__ == '__main__':
    init_db().create_all(app=app)
    app.run(debug=True)

