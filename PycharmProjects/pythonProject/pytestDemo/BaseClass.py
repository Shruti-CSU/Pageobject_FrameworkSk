import inspect
import logging



class BaseClass:
    def getlog(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # This is to print message in format
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
