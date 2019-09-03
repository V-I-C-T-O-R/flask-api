from flask import Flask
import logging
from datetime import timedelta
from logging.handlers import TimedRotatingFileHandler
from flask_jwt import JWT
from robot.auth.secutiry import authenticate, identity

__author__='victor'

def get_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hc2018happynewyear"
    # app.response_class = Response
    return app

def auth_access(app,config=None):
    # jwt访问验证
    jwt = JWT(app, authenticate, identity)  # http://localhost:5000/auth
    if config is None:
        return
    app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=config.JTW_EXPIRE_TIME)

def init_logger(config):
    # 日志系统配置
    logging.basicConfig(level=logging.DEBUG, format=config.FLASK_LOGGER_FORMAT, datefmt=config.FLASK_LOGGER_DATE_FORMAT)
    handler = TimedRotatingFileHandler(filename=config.FLASK_LOGGER_FILE+'info.log', when="D", interval=1, backupCount=7,encoding=config.FLASK_LOGGER_CHARSET)

    formatter = logging.Formatter(config.FLASK_LOGGER_FORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(config.FLASK_LOGGER_LEVEL)

    app.logger.handlers.clear()
    app.logger.addHandler(handler)

def init_gunicorn_logger(config):
    gunicorn_logger = logging.getLogger('gunicorn.error')
    gunicorn_logger.setLevel(logging.DEBUG)
    gunicorn_logger.handlers.clear()

    handler = TimedRotatingFileHandler(filename=config.FLASK_LOGGER_FILE + 'info.log', when="D", interval=1,
                                       backupCount=5, encoding=config.FLASK_LOGGER_CHARSET)

    formatter = logging.Formatter(config.FLASK_LOGGER_FORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(config.FLASK_LOGGER_LEVEL)
    gunicorn_logger.addHandler(handler)
    return gunicorn_logger

app = get_app()