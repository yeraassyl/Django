import logging

logger = logging.getLogger('logger_sample')
logger.setLevel(logging.DEBUG)


console_handler = logging.StreamHandler()

test_message = 'Someone'

logging.debug(f'debug message shows: {test_message}')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')