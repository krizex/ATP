import logging

def getLogger(appName):
    logger = logging.getLogger(appName)
    logger.setLevel(logging.DEBUG)
    
    fhDebug = logging.FileHandler(appName + "_debug.log")
    fhDebug.setLevel(logging.DEBUG)
    
    fhRun = logging.FileHandler(appName + "_run.log")
    fhRun.setLevel(logging.ERROR)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
    for i in (fhDebug, fhRun, ch):
        i.setFormatter(formatter)
        logger.addHandler(i)
        
    return logger