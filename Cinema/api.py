from flask_restful import Api

from Cinema.views.cinema_views import CinemaResource
from Cinema.views.hall_views import HallResource
from Cinema.views.user_views import CinemaUserResource

Cinema_api = Api(prefix="/cinema")
Cinema_api.add_resource(CinemaUserResource, '/users/')
Cinema_api.add_resource(CinemaResource, '/cinemas/')
Cinema_api.add_resource(HallResource, '/halls/')
