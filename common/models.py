from flask import current_app

from FlaskTpp.ext import db


class PrimaryKeyBaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            return False
        return True
