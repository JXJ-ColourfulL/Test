import caching
from flask import request, current_app
from flask_restful import Resource, reqparse

from Admin.models.user_model import AdminUser
from FlaskTpp.ext import cache
from FlaskTpp.settings import ADMIN_USER_TOKEN_CACHE_TIME
from common.token import generate_admin_token

parser = reqparse.RequestParser()
parser.add_argument('u_name', type=str, required=True, help='Rate cannot be converted')
parser.add_argument('u_password', type=str, required=True, help='aaaa')


class UserResource(Resource):

    def post(self):
        # 获取
        action = request.args.get("action")
        if action == "login":
            return self.do_login()
        elif action == "register":
            return self.do_register()
        else:
            data = {
                "msg": "action err",
                "status": 400
            }
            return data

    def do_login(self):
        args = parser.parse_args()
        u_name = args.get("u_name")
        u_password = args.get("u_password")
        try:
            user = AdminUser.query.filter(AdminUser.u_name == u_name).first()
        except Exception as e:
            current_app.logger.errot(e)
            data = {
                "msg": "user is not exist",
                "status": 401
            }
            return data
        else:
            if not user:
                data = {
                    "msg": "user is not exist",
                    "status": 401
                }
                return data

        if not user.verity_password(u_password):
            data = {
                "msg": "Incorrect user name or password",
                "status": 401
            }
            return data
        token = generate_admin_token()
        cache.set(token, user.id, timeout=ADMIN_USER_TOKEN_CACHE_TIME)
        data = {
            "msg": "login success",
            "status": 200,
            "token": token
        }
        return data

    def do_register(self):

        args = parser.parse_args()
        u_name = args.get("u_name")
        u_password = args.get("u_password")

        user = AdminUser()
        user.u_name = u_name
        user.u_password = u_password

        if not user.save():
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
