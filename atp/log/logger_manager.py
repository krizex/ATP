import logging
import sys

def getLogger(appName):
    logger = logging.getLogger(appName)
    logger.setLevel(logging.DEBUG)
    
    fhDebug = logging.FileHandler(appName + "_debug.log")
    fhDebug.setLevel(logging.DEBUG)
    
    fhRun = logging.FileHandler(appName + "_run.log")
    fhRun.setLevel(logging.INFO)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
    for i in (fhDebug, fhRun, ch):
        i.setFormatter(formatter)
        logger.addHandler(i)
        
    return logger