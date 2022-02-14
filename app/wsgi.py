import logging

from app import app


logging.basicConfig(format='[%(levelname)s] - %(message)s',
                    level=logging.INFO)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.info')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == '__main__':
    app.run()
