from flask import *

from mycards.controllers.user import user_blueprint
from mycards.controllers.card import card_blueprint
from mycards.model import db


app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(card_blueprint)
app.__version__ = '0.1.0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret key"
app.config['AUTHORIZATION_ALGORITHM'] = 'HS256'
db.init_app(app)


@app.route('/version')
def version():
    return app.__version__


if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)

