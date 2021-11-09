import logging


def getLog(nm):
    logger = logging.getLogger(nm)
    f = open("properties.txt", 'r')
    if f.mode == 'r':
        loglevel = f.read()
    if loglevel == "ERROR":
        logger.setLevel(logging.ERROR)
    elif loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    # creating formatter
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    # creating handlers
    file_handler = logging.FileHandler('test.log')
    #adding formatters to handlers
    file_handler.setFormatter(formatter)
    #adding handlers to logger
    logger.addHandler(file_handler)
    return logger
