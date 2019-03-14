from Admin.api import admin_api
from Cinema.api import Cinema_api


def init_api(app):
    admin_api.init_app(app)
    Cinema_api.init_app(app)