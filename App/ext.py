from flask_migrate import Migrate
from flask_session import Session

from App.models import db
from App.views import blue


def init_ext(app):
    app.register_blueprint(blueprint=blue)
    Migrate(app=app, db=db)
    Session(app=app)