
from flask_script import Manager

import run

application = run.app
manager = Manager(application)

@manager.command
def prod():
    from setting import ProdConfig
    prod = ProdConfig
    run.init_logger(prod)
    application.logger.info('app load jwt module')
    run.auth_access(application,prod)
    application.logger.info('app running at %s:%s ,env=%s ,debug=%s' % (prod.FLASK_HOST, prod.FLASK_PORT,prod.FLASK_ENV, prod.FLASK_DEBUG))
    application.run(debug=prod.FLASK_DEBUG, host=prod.FLASK_HOST, port=prod.FLASK_PORT)

@manager.command
def dev():
    from setting import DevConfig
    dev = DevConfig
    run.init_logger(dev)
    application.logger.info('app load jwt module')
    run.auth_access(application,dev)
    application.logger.info('application running at %s:%s ,env=%s ,debug=%s' % (dev.FLASK_HOST, dev.FLASK_PORT,dev.FLASK_ENV, dev.FLASK_DEBUG))
    application.run(debug=dev.FLASK_DEBUG, host=dev.FLASK_HOST, port=dev.FLASK_PORT)

@manager.command
def debug():
    from setting import TestConfig
    test = TestConfig
    run.init_logger(test)
    application.logger.info('application load jwt module')
    run.auth_access(application,test)
    application.logger.info('application running at %s:%s ,env=%s ,debug=%s' % (test.FLASK_HOST, test.FLASK_PORT,test.FLASK_ENV, test.FLASK_DEBUG))
    application.run(debug=test.FLASK_DEBUG, host=test.FLASK_HOST, port=test.FLASK_PORT)

if __name__ == '__main__':
    manager.run()
