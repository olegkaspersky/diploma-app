import multiprocessing

# pidfile = 'nhl-app.pid'
# proc_name = 'nhl-app'

bind = '0.0.0.0:5000'

workers = (2 * multiprocessing.cpu_count()) + 1
threads = 2 * multiprocessing.cpu_count()
worker_class = 'gthread'
worker_tmp_dir = '/dev/shm'

timeout = 30
keepalive = 5


# logging config section
accesslog = '-'
access_log_format = '%(r)s %(s)s %(a)s'

errorlog = '-'
loglevel = 'warning'

# ! logconfig = '-'
