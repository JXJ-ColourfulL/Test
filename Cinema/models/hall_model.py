from Cinema.models.cinema_model import Cinema
from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel


class Hall(PrimaryKeyBaseModel):
    h_num = db.Column(db.String(32))
    h_mode = db.Column(db.String(32))
    h_seats = db.Column(db.String(256))
    h_cinema = db.Column(db.ForeignKey(Cinema.id))