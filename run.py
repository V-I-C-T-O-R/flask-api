from setting import TestConfig,ProdConfig,DevConfig
import setting
from robot import app, init_logger, auth_access, init_gunicorn_logger

if __name__ == '__main__':
    import sys,os
    if len(sys.argv) > 2:
        print('参数个数不正确,请检查')
        sys.exit()
    elif len(sys.argv) == 1:
        config = TestConfig
    elif sys.argv[1] == 'dev':
        config = DevConfig
    elif sys.argv[1] == 'prod':
        config = ProdConfig
    else:
        config = TestConfig

    init_logger(config)
    app.cfg = config
    app.logger.info('app load jwt module')
    auth_access(app,config)
    app.logger.info('app load route api module')
    from robot import api
    app.logger.info('app running at %s:%s ,env=%s ,debug=%s'%(config.FLASK_HOST,config.FLASK_PORT,config.FLASK_ENV,config.FLASK_DEBUG))
    #可设置use_reloader=False,目的是为了只加载一次代码
    app.run(debug=config.FLASK_DEBUG, host=config.FLASK_HOST,port=config.FLASK_PORT)
else:
    '''
        线上注意转换成ProConfig
    '''
    # config = TestConfig
    config = ProdConfig

    gunicorn_logger = init_gunicorn_logger(config)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    app.logger.info('app load jwt module')
    auth_access(app, config)
    app.cfg = config
    app.logger.info('app load route api module')
    from robot import api