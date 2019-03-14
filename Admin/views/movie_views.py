from flask import request, current_app
from flask_restful import Resource, fields, marshal, marshal_with

from Admin.models.movie_model import Movie
from decorators import login_required

movie_fiedls = {
    "id": fields.Integer,
    "m_name": fields.String,
    "m_duration": fields.Integer,
    "m_type": fields.String
}

get_movie_fiedls = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(movie_fiedls))
}


class MovieResource(Resource):
    # 获取所有电影信息
    @marshal_with(get_movie_fiedls)
    def get(self):
        try:
            movies = Movie.query.all()
        except Exception as e:
            current_app.logger.error(e)
            data = {
                "msg": "query failed",
                "status": 401,
            }
            return data
        data = {
            "msg": "ok",
            "status": 200,
            "data": movies
        }
        return data

    # 添加电影信息
    # 是否登陆
    @login_required
    def post(self):
        m_name = request.form.get("m_name")
        m_duration = request.form.get("m_duration")
        m_type = request.form.get("m_type")

        movie = Movie()

        movie.m_name = m_name
        movie.m_duration = m_duration
        movie.m_type = m_type

        if not movie.save():
            data = {
                "msg": "save fail",
                "status": 401
            }
            return data
        data = {
            "msg": "save success",
            "status": 200,
            "data": marshal(movie, movie_fiedls)
        }
        return data


