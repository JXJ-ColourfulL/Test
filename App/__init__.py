import os
from flask import Flask

from App import settings
from App.ext import init_ext


def create_app(name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    template_folder = os.path.join(BASE_DIR, 'templates')

    static = os.path.join(BASE_DIR, 'static')

    app = Flask(__name__,template_folder=template_folder,static_folder=static)
    app.config.from_object(settings.NEV_NAME.get(name))
    init_ext(app)
    return app