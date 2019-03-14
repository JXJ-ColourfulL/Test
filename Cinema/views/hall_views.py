from flask import g, request
from flask_restful import Resource, fields, marshal

from Cinema.models.cinema_model import Cinema
from Cinema.models.hall_model import Hall
from Cinema.models.user_model import PERMISSION_READ
from decorators import permission_required

hall_fields = {
    "id": fields.Integer,
    "h_num": fields.String,
    "h_seats": fields.String,
    "h_mode": fields.String,
    "h_cinema": fields.Integer
}


class HallResource(Resource):

    @permission_required(PERMISSION_READ)
    def post(self):
        # 创建大厅
        #          用户必须登入
        #           需要权限
        #
        #         验证对象权限 对象是用户的

        # 获取user对象
        user = g.user
        # 获取传参
        h_num = request.form.get("h_num")
        h_seats = request.form.get("h_seats")
        h_mode = request.form.get("h_mode")
        h_cinema = request.form.get("h_cinema")

        # cinema = Cinema.query.get(h_cinema)
        # if cinema.c_user != user.id:

        # 判断用户添加影厅的影院是否是自己名下的
        cinemas = Cinema.query.filter(Cinema.c_user.__eq__(user.id)) \
            .filter(Cinema.id == h_cinema).first()
        # 如果不是 直接返回
        if not cinemas:
            data = {
                "msg": "bushuyu",
                "status": 401,
            }
            return data

        # 添加影厅保存
        hall = Hall()
        hall.h_num = h_num
        hall.h_mode = h_mode
        hall.h_seats = h_seats
        hall.h_cinema = h_cinema

        if not hall.save():
            data = {
                "msg": "save failed",
                "status": 401
            }
            return data
        data = {
            "msg": "create success",
            "status": 200,
            "data": marshal(hall, hall_fields)
        }
        return data
