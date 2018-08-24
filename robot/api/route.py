from flask_restful import Api

from robot.handle import common_handle


def route_api(app):
    api = Api(app)
    api.add_resource(common_handle.XmHandler, "/xml")
    # api.add_resource(common_handle.Robot, "/robot")

