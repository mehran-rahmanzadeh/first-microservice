import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connection = 1000
timeout = 2

preload_app = True
daemon = False

# user = 'django'
# group = 'django'

# ssl
# keyfile=
# certfile=
# ssl_version=

# log
accesslog = '/var/log/gunicorn/access.log'
# log_level = 'info'
# access_log_format =
errorlog = '/var/log/gunicorn/error.log'

# debug
reload = False
reload_engine = 'auto'
# reload_extra_file = []
