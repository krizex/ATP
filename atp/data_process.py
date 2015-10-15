import qunar
import time
from dbc import DB
from flight_info import FlightInfoHandler, FlightInfo
from errcode import *

def processDataByFile(fileName, depDate):
    curDateTime =  time.localtime(time.time())
    
    queryDate = time.strftime('%Y-%m-%d', curDateTime)
    queryTime = time.strftime('%H:%M:%S', curDateTime)
    
    retList = qunar.analysis(fileName)
    
    db = DB('atp', 'atp', 'atp')
    conn = db.getConn()
    if not conn:
        print "connect db failed."
        return ER_CONN_DB_FAILED
    
    handler = FlightInfoHandler(conn)
    
    for rec in retList:
        flightInfo = FlightInfo(queryDate, queryTime, depDate, rec)
        handler.insertOneRec(flightInfo)
        
    return ER_SUCC

