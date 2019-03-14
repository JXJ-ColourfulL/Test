from flask_restful import Api




# 创建user Api实例
from Admin.views.movie_views import MovieResource
from Admin.views.user_views import UserResource

admin_api = Api(prefix="/admin")
admin_api.add_resource(UserResource, '/users/')
admin_api.add_resource(MovieResource, '/movie/')