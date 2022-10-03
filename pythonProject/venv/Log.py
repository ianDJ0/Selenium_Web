import time
import logging

logging.basicConfig(filename='D:\SeleniumDownloadLocation/testlog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p'
                    )
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("This is debugging message")
logging.info("This is a message")
logging.warning("This is warning message")
logging.error("There is an error")
logging.critical("Critical error please fix!")
