import logging
import logging.handlers

file_name = 'logs/sample_api.log'


def set_file_name(val):
    global file_name
    file_name = val


def get_file_name():
    global file_name
    return {'file': file_name}


class CustomLogger(logging.Logger):

    def _log(self, level, msg, args, exc_info=None, extra=None, **kwargs):
        if extra is None:
            extra = get_file_name()
        super(CustomLogger, self)._log(level, msg, args, exc_info, extra)


class Logger:
    @staticmethod
    def get_logger(logger_name):
        log_level = logging.INFO
        log_format = f'%(asctime)-15s - ifdpOncall - %(name)s - %(levelname)-8s %(message)s'
        logging.setLoggerClass(CustomLogger)
        logging.basicConfig(level=log_level, format=log_format, filename=file_name)
        logger = logging.getLogger(logger_name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - [source_file=%(file)s] - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
