import datetime
from operator import or_, and_

from flask import g, request
from flask_restful import Resource, fields, marshal

from Admin.models.movie_model import Movie
from Cinema.models.cinema_model import Cinema
from Cinema.models.hall_model import Hall
from Cinema.models.order_model import PAY_TO_COMPLETE, MovieOrder
from Cinema.models.schedule_model import Schedule
from Cinema.models.user_model import PERMISSION_WRITE, CinemaUser
from decorators import permission_required

# 清扫时间 单位：分
CLEANING_TIME = 15
schedule_fields = {
    "id": fields.Integer,
    "hall_id": fields.Integer,
    "movie_id": fields.Integer,
    "movie_start_time": fields.DateTime,
    "movie_end_time": fields.DateTime,
    "movie_price": fields.Float
}


class ScheduleResource(Resource):

    # 添加排档
    @permission_required(PERMISSION_WRITE)
    def post(self):
        # 检验是否登入
        # 检验是否有权限
        # 获取参数
        user = g.user
        hall_id = request.form.get("hall_id")
        movie_id = request.form.get("movie_id")
        movie_start_time = request.form.get("movie_start_time")
        movie_price = request.form.get("movie_price")

        # 校验放映厅是否是该用户
        hall = Hall.query.get(hall_id)
        cinema = Cinema.query.get(hall.h_cinema)

        if user.id != cinema.c_user:
            data = {
                "msg": "hall falseness",
                "status": 401
            }
            return data

        # 校验是否已经购买该影片
        orders = MovieOrder.query.filter(MovieOrder.o_user.__eq__(user.id)) \
            .filter(Movie.id.__eq__(movie_id)) \
            .filter(MovieOrder.o_status == PAY_TO_COMPLETE).first()
        if not orders:
            data = {
                "msg": "No right to play",
                "status": 401
            }
            return data

        schedule = Schedule()
        schedule.hall_id = hall_id
        schedule.movie_id = movie_id
        schedule.movie_price = movie_price
        schedule.movie_start_time = movie_start_time
        # 生成结束时间
        movie_duration = Movie.query.get(movie_id).m_duration
        data, time = movie_start_time.split(" ")
        year, month, day = data.split("-")
        hour, minute, second = time.split(":")

        movie_start_time_tran = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour),
                                                  minute=int(minute), second=int(second))
        movie_end_time = movie_start_time_tran + datetime.timedelta(minutes=movie_duration) + datetime.timedelta(
            minutes=CLEANING_TIME)
        schedule.movie_end_time = movie_end_time
        # 校验该时间段是否可以排档
        # schedule_left = Schedule.query.filter(Schedule.movie_start_time.__le__(movie_end_time).filter(
        #     Schedule.movie_end_time.__ge__(movie_end_time))
        # schedule_right = Schedule.query.filter(
        #     Schedule.movie_start_time.__le__(movie_start_time).filter(Schedule.movie_end_time.__ge__(movie_start_time)))
        # schedule_contains = Schedule.query.filter(
        #     Schedule.movie_start_time.__ge__(movie_start_time).filter(Schedule.movie_end_time.__le__(movie_end_time)))
        #
        # if all([schedule_contains, schedule_left, schedule_right]):

        schedules = Schedule.query.filter(
            or_(
                or_(
                    and_(
                        Schedule.movie_start_time.__le__(
                            movie_end_time
                        ),
                        Schedule.movie_end_time.__ge__(
                            movie_end_time
                        )
                    ),
                    and_(
                        Schedule.movie_start_time.__le__(
                            movie_start_time
                        ),
                        Schedule.movie_end_time.__ge__(
                            movie_start_time
                        )
                    )
                ),
                and_(
                    Schedule.movie_start_time.__ge__(
                        movie_start_time
                    ),
                    Schedule.movie_end_time.__le__(
                        movie_end_time
                    )
                )
            )
        )
        if schedules.first():
            data = {
                "msg": "Time conflict",
                "status": 403
            }
            return data
        if not schedule.save():
            data = {
                "msg": "create failed",
                "status": 401,
            }
            return data

        data = {
            "msg": "create success",
            "status": 200,
            "data": marshal(schedule, schedule_fields)
        }
        return data

    def get(self):
        cinema_id = request.args.get("cinema_id")
        movie_id = request.args.get("movie_id")
        data_time = request.args.get("data_time")

        halls = Hall.query.filter(Hall.h_cinema.__eq__(cinema_id))
        hall_id = [hall.id for hall in halls]

        scheduless = Schedule.query.filter(Schedule.movie_id.__eq__(movie_id)) \
            .filter(Schedule.hall_id.in_(hall_id)) \
            .filter(Schedule.movie_start_time.__ge__(data_time + " 00:00:00")) \
            .filter(Schedule.movie_start_time.__le__(data_time + " 23:59:59")).all()
        data = {
            "msg": "ok",
            "status": 200,
            "data": marshal(scheduless, schedule_fields)
        }
        return data
