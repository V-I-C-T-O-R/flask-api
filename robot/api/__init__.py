__author__ = 'victor'

from robot import app
from . import common_api,route

route.route_api(app)
common_api.register_api(app)