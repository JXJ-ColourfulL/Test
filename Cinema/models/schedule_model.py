from Admin.models.movie_model import Movie
from Cinema.models.hall_model import Hall
from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel


class Schedule(PrimaryKeyBaseModel):
    hall_id = db.Column(db.ForeignKey(Hall.id))
    movie_id = db.Column(db.ForeignKey(Movie.id))
    movie_start_time = db.Column(db.DateTime)
    movie_end_time = db.Column(db.DateTime)
    movie_price = db.Column(db.Float, default=90)
