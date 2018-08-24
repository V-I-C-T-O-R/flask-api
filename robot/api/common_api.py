from flask import Blueprint
from flask_jwt import jwt_required

api = Blueprint('api',__name__)

@api.route('/', methods=['GET', ])
# @jwt_required()
def show():
    return 'hello world',200

def register_api(app):
    app.register_blueprint(api)