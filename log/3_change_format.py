import logging

logging.basicConfig(
	filename = 'format2.log',
	level = logging.DEBUG,
	format = '%(asctime)s - %(levelname)s - %(message)s',
	datefmt = '%m/%d/%Y %I:%M:%S %p'
)

logging.warning('is when this event was logged.')
