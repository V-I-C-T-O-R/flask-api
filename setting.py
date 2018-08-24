import logging
import os

class Config(object):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # 全局配置文件
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = 5001
    FLASK_DEBUG = True

    # jtw消息过期时间
    JTW_EXPIRE_TIME = 3600

    # log配置
    FLASK_LOGGER_LEVEL = logging.INFO
    FLASK_LOGGER_FORMAT = '%(asctime)s-%(levelname)s-%(filename)s-%(lineno)s: %(message)s'
    FLASK_LOGGER_FILE = current_dir + '/logs/'
    FLASK_LOGGER_CHARSET = 'utf8'
    FLASK_LOGGER_SUFFIX = '%Y-%m-%d.log'
    FLASK_LOGGER_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ProdConfig(Config):
    """Production configuration."""
    FLASK_ENV = 'prod'
    FLASK_DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    FLASK_ENV = 'dev'
    FLASK_DEBUG = True

class TestConfig(Config):
    """Test configuration."""
    FLASK_ENV = 'test'
    FLASK_TESTING = True
    FLASK_DEBUG = True