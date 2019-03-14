from werkzeug.security import generate_password_hash, check_password_hash

from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel

PERMISSION_READ = 1
PERMISSION_WRITE = 2
PERMISSION_DELETE = 4
PERMISSION_PLACE = 8


class CinemaUser(PrimaryKeyBaseModel):
    cu_name = db.Column(db.String(64), unique=True)
    _cu_password = db.Column(db.String(128))
    cu_permissions = db.Column(db.Integer, default=PERMISSION_READ)
    c_cinema = db.relationship("Cinema", backref="CinemaUser", lazy=True)

    @property
    def cu_password(self):
        raise Exception("只读")

    @cu_password.setter
    def cu_password(self, password):
        self._cu_password = generate_password_hash(password)

    def verity_password(self, password):
        return check_password_hash(self._cu_password, password)

    def check_permissions(self, permissions):
        return self.cu_permissions & permissions == permissions
