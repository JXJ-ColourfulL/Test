from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel


class Movie(PrimaryKeyBaseModel):
    m_name = db.Column(db.String(64), unique=True)
    m_duration = db.Column(db.Integer, default=90)
    m_type = db.Column(db.String(32))

