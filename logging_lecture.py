import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\Users\\a\\Desktop\\advance\\ul.log", 
                    level=logging.ERROR,
                    filemode='w',
                    format=LOG_FORMAT)
logger = logging.getLogger()

logger.debug("Message from debug level")
logger.info("Message from info level")
logger.warning("Message from warning level")
logger.error("Message from error level")
logger.critical("Message from critical level")