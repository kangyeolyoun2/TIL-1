import logging

logging_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='format.log',level=logging.DEBUG,format=logging_format)
logging.warning('is when this event was logged.')
