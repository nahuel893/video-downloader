import logging
from os import path
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
    def __init__(self, name, level=None):

        # Setting name of log file
        self.filename = f'{name}.log'
        # Setting folder for log files
        self.file_path = path.join(
                path.dirname(__file__),
                'logs', self.filename
                )
        print('PATH:', self.file_path)

        # Get the logger instance
        self.logger = logging.getLogger(name)

        # Set filehandler for create log file in logs/ folder, and set format
        fh = logging.FileHandler(filename=self.file_path, mode='a')
        ft = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        fh.setFormatter(ft)
        self.logger.addHandler(fh)

        # Set personalized level
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
