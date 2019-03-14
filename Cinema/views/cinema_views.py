from flask import request, g
from flask_restful import Resource, fields, marshal

from Cinema.models.cinema_model import Cinema
from Cinema.models.user_model import PERMISSION_WRITE, PERMISSION_READ
from decorators import login_required, permission_required

cinema_fields = {
    'id': fields.Integer,
    'c_name': fields.String,
    'c_address': fields.String,
    'c_phone': fields.String
}


class CinemaResource(Resource):
    @login_required
    def get(self):
        cinema = Cinema.query.all()
        data = {
            "msg": "ok",
            "status": 200,
            "data": marshal(cinema, cinema_fields)
        }
        return data

    @permission_required(PERMISSION_READ)
    def post(self):
        user_id = g.user.id
        c_name = request.form.get("c_name")
        c_address = request.form.get("c_address")
        c_phone = request.form.get("c_phone")

        cinema = Cinema()
        cinema.c_name = c_name
        cinema.c_address = c_address
        cinema.c_phone = c_phone
        cinema.c_user = user_id

        if not cinema.save():
            data = {
                "msg": "save failed",
                "status": 401
            }
            return data
        data = {
            "msg": "ok",
            "status": 200,
            "data": marshal(cinema, cinema_fields)
        }
        return data
