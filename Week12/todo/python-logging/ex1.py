import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='example.log',
    filemode='a', # write append
    format = '%(levelname)s -- %(levelno)s -- %(message)s',
)

test_message = 'Someone'

logging.debug(f'debug message shows: {test_message}')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')