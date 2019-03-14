from werkzeug.security import generate_password_hash, check_password_hash

from FlaskTpp.ext import db
from common.models import PrimaryKeyBaseModel


class AdminUser(PrimaryKeyBaseModel):
    u_name = db.Column(db.String(32), unique=True)
    _u_password = db.Column(db.String(128))

    @property
    def u_password(self):
        raise Exception("密码不可读")

    @u_password.setter
    def u_password(self, password):
        self._u_password = generate_password_hash(password)

    def verity_password(self, password):
        return check_password_hash(self._u_password, password)
