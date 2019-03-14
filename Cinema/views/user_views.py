from flask import request, current_app
from flask_restful import Resource, reqparse

from Cinema.models.user_model import CinemaUser
from FlaskTpp.ext import cache
from FlaskTpp.settings import CINEMA_USER_TOKEN_CACHE_TIME
from common.token import generate_cinema_token

parser = reqparse.RequestParser()
parser.add_argument('cu_name', type=str, required=True, help='Rate cannot be converted')
parser.add_argument('cu_password', type=str, required=True, help='aaaa')


class CinemaUserResource(Resource):
    def post(self):
        action = request.args.get("action")
        if action == "login":
            return self.do_login()
        elif action == "register":
            return self.do_register()
        else:
            data = {
                "msg": "action err",
                "status": 401
            }
            return data

    def do_register(self):
        cu_name = request.form.get("cu_name")
        cu_password = request.form.get("cu_password")

        c_user = CinemaUser()

        c_user.cu_name = cu_name
        c_user.cu_password = cu_password

        if not c_user.save():
            data = {
                "msg": "register fail",
                "status": 400
            }
            return data

        data = {
            "msg": "register success",
            "status": 201,
        }
        return data

    def do_login(self):
        args = parser.parse_args()
        cu_name = args.get("cu_name")
        cu_password = args.get("cu_password")

        print(cu_name)

        c_user = CinemaUser.query.filter(CinemaUser.cu_name.__eq__(cu_name)).first()

        if not c_user:
            data = {
                "msg": "user is not exist",
                "status": 401
            }
            return data
        if not c_user.verity_password(cu_password):
            data = {
                "msg": "Incorrect user name or password",
                "status": 401
            }
            return data
        token = generate_cinema_token()
        cache.set(token, c_user.id, timeout=CINEMA_USER_TOKEN_CACHE_TIME)
        data = {
            "msg": "login success",
            "status": 200,
            "token": token
        }
        print("1111")
        print(data)
        return data

