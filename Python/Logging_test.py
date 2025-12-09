#Testing logging

import logging

from torch import le

#Creates log file
logging.basicConfig(
    filename = 'pythonlog.log',
    filemode= 'w', #Sets file mode to write to avoid duplication of file
    
    level = logging.DEBUG,
    format = '[%(levelname)s] %(message)s'
)

#Create logging levels and names
TRACE = 5
INFO = 10
DEBUG = 20
WARNING = 30
ERROR = 40
FATAL = 60
logging.addLevelName(TRACE, 'TRACE')
logging.addLevelName(INFO, 'INFO')
logging.addLevelName(DEBUG, 'DEBUG')
logging.addLevelName(WARNING, 'WARNING')
logging.addLevelName(FATAL, 'FATAL')   

#Create logging functions and pass parameters if not found yet, args passes position arguments, kwargs passes keywords as arguments

def trace(message, *args, **kwargs):
    logging.log(TRACE, message, *args, **kwargs)

def fatal(message, *args, **kwargs):
    logging.log(FATAL, message, *args, **kwargs)

def warn(message, *args, **kwargs):
    logging.warning(message, *args, **kwargs)

def info(message, *args, **kwargs):
    logging.info(message, *args, *kwargs)

def debug(message, *args, **kwargs):
    logging.debug(message, *args, **kwargs)

def error(message, *args, **kwargs):
    logging.error(message, *args, **kwargs)

#Example usage of logging levels
fatal("Fatal error, shutting down")
warn("Issue occured, please check")