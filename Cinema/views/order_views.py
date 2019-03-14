from flask import request, g
from flask_restful import Resource

from Admin.models.movie_model import Movie
from Cinema.models.order_model import MovieOrder, PAY_TO_COMPLETE, NON_PAYMENT
from Cinema.models.user_model import PERMISSION_PLACE, CinemaUser
from decorators import permission_required


class MovieOrderResource(Resource):
    @permission_required(PERMISSION_PLACE)
    def post(self):
        # 验证用户是否登入和是否有下单权限
        # 验证电影是否存在
        user = g.user
        movie_id = request.form.get("movie_id")

        movie = Movie.query.filter(Movie.id == movie_id).first()
        # 如果不存在 直接返回
        if not movie:
            data = {
                "msg": "movie not exist",
                "status": 401
            }
            return data
        # 订单已经支付完成
        orders = MovieOrder.query.filter(MovieOrder.o_user.__eq__(user.id))\
                                 .filter(Movie.id.__eq__(movie_id))\
                                 .filter(MovieOrder.o_status == PAY_TO_COMPLETE).first()
        if orders:
            data={
                "msg":"In order to buy",
                "status": 401
            }
            return data
        # 订单是否存在但未支付
        orders = MovieOrder.query.filter(MovieOrder.o_user.__eq__(user.id)) \
                                 .filter(Movie.id.__eq__(movie_id)) \
                                 .filter(MovieOrder.o_status == NON_PAYMENT).first()

        if orders:
            data={
                "msg":"Order to exist",
                "status": 401,
            }
            return data


        # 创建movie订单
        movie_order = MovieOrder()
        movie_order.o_movie = movie_id
        movie_order.o_user = user.id
        # 保存至数据库
        if not movie_order.save():
            data = {
                "msg": "create failed",
                "status": 401
            }
            return data
        data = {
            "msg": "create success",
            "status": 200
        }
        return data
