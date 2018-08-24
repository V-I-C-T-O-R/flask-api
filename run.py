import logging
from datetime import timedelta
from logging.handlers import TimedRotatingFileHandler

from flask_jwt import JWT
import setting
from robot.auth.secutiry import authenticate, identity
from robot import app


def auth_access(app,config=None):
    # jwt访问验证
    jwt = JWT(app, authenticate, identity)  # http://localhost:5000/auth
    if config is None:
        return
    app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=config.JTW_EXPIRE_TIME)

def init_logger(config):
    # 日志系统配置
    logging.basicConfig(level=config.FLASK_LOGGER_LEVEL, format=config.FLASK_LOGGER_FORMAT, datefmt=config.FLASK_LOGGER_DATE_FORMAT)
    logger = logging.getLogger(__name__)
    logger.setLevel(config.FLASK_LOGGER_LEVEL)
    handler = TimedRotatingFileHandler(filename=config.FLASK_LOGGER_FILE+'info.log', when="D", interval=1, backupCount=7,encoding=config.FLASK_LOGGER_CHARSET)

    formatter = logging.Formatter(config.FLASK_LOGGER_FORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(config.FLASK_LOGGER_LEVEL)
    logger.handlers.clear()
    logger.addHandler(handler)
    app.logger.handlers = logger.handlers
    # return logger

if __name__ == '__main__':
    config = setting.ProdConfig
    init_logger(config)
    app.logger.info('app load jwt module')
    auth_access(app,config)
    app.logger.info('app load route api module')
    from robot import api
    app.logger.info('app running at %s:%s ,env=%s ,debug=%s'%(config.FLASK_HOST,config.FLASK_PORT,config.FLASK_ENV,config.FLASK_DEBUG))
    app.run(debug=config.FLASK_DEBUG, host=config.FLASK_HOST,port=config.FLASK_PORT)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    config = setting.ProdConfig
    auth_access(app,config)
    from robot import api