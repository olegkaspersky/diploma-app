import multiprocessing

bind = '0.0.0.0:5000'
workers = (2 * multiprocessing.cpu_count()) + 1
worker_class = 'gthread'
threads = 2 * multiprocessing.cpu_count()


# logging config section
accesslog = '-'
access_log_format = '%(r)s %(s)s %(a)s'

errorlog = '-'
loglevel = 'warning'

# ! logconfig = '-'
