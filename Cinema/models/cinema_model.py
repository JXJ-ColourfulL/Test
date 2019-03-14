from Cinema.models.user_model import CinemaUser
from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel


class Cinema(PrimaryKeyBaseModel):
    c_name = db.Column(db.String(64))
    c_address = db.Column(db.String(256))
    c_phone = db.Column(db.String(64))
    c_user = db.Column(db.ForeignKey(CinemaUser.id))