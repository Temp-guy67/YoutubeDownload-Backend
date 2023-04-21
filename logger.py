import logging


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a stream handler to write logs to console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Create a formatter to format the log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

# Add the stream handler to the logger
logger.addHandler(stream_handler)