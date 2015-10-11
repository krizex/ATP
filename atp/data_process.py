from atp import qunar
import time

def processDataByFile(fileName):
    retList = qunar.analysis(fileName)
    curDateTime =  time.localtime(time.time())
    
    queryDate = time.strftime('%Y-%m-%d', curDateTime)
    quertTime = time.strftime('%H:%M:%S', curDateTime)
    
    print queryDate, quertTime
    for rec in retList:
        print rec