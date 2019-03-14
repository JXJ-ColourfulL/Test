from flask import request, current_app, g

from Admin.models.user_model import AdminUser
from Cinema.models.user_model import CinemaUser
from FlaskTpp.ext import cache


def login_required(fun):
    def wrapper(*args, **kwargs):
        try:
            token = request.args.get("token")
            user_id = cache.get(token)
            user = AdminUser.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)
            data = {
                "msg": "query fail",
                "status": 401
            }
            return data
        if not user:
            data = {
                "msg": "not login",
                "status": 401
            }
            return data
        return fun(*args, **kwargs)

    return wrapper


def permission_required(permission):
    def login_required(fun):
        def wrapper(*args, **kwargs):
            try:
                token = request.args.get("token")
                user_id = cache.get(token)
                user = CinemaUser.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)
                data = {
                    "msg": "query fail",
                    "status": 401
                }
                return data
            if not user:
                data = {
                    "msg": "not login",
                    "status": 401
                }
                return data
            if not user.check_permissions(permission):
                data = {
                    "msg": "not peimission",
                    "status": 401
                }
                return data
            g.user = user
            return fun(*args, **kwargs)

        return wrapper

    return login_required
