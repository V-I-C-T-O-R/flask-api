import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing
current_dir = os.path.abspath(os.path.dirname(__file__))
debug = True
loglevel = 'info'
bind = '0.0.0.0:5001'
threads = 2
timeout = 30
backlog = 512
pidfile = current_dir+'/logs/gunicorn.pid'
accesslog=current_dir+'/logs/access.log'
errorlog=current_dir+'/logs/error.log'

#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'