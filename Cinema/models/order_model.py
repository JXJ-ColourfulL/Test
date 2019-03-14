from datetime import datetime

from Admin.models.movie_model import Movie
from Cinema.models.user_model import CinemaUser
from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel

NON_PAYMENT = 0


class MovieOrder(PrimaryKeyBaseModel):
    o_movie = db.Column(db.ForeignKey(Movie.id))
    o_user = db.Column(db.ForeignKey(CinemaUser.id))
    o_create_time = db.Column(db.DateTime, default=datetime.now())
    o_status = db.Column(db.String, default=NON_PAYMENT)
