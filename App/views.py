
from flask import Blueprint, render_template

blue = Blueprint('first',__name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/aa/')
def aa():
    return render_template('Support.html')