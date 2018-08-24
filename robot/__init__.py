from flask import Flask

__author__='victor'

def get_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hc2018happynewyear"
    # app.response_class = Response
    return app

app = get_app()