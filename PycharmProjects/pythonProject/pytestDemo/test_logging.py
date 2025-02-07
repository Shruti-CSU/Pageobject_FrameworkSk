import logging


def test_loggingprint():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # This is to print message in format
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # Add handler use to fetch file location and it will only accept fileHandler

   # loger.setLevel(logging.INFO) # This means only after info level will be printed
    logger.debug("This is debug statement")
    logger.info("Information Statement")
    logger.warning("Warning Message")
    logger.error("This is the error in script")
    logger.critical("This is critical blocker in script")