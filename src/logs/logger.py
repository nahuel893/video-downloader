import logging

levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
        }

logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(message)s',
        level=levels['debug']
        )



class MyLogger:
    def __init__(self, name, level):
        self.logger = logging.getLogger(name)
        if level:
            self.logger.setLevel(levels[level])

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    logger = MyLogger('logger')
    logger.debug('Test logger')
