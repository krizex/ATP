import qunar
import time
from dbc import DB
from flight_info import FlightInfoHandler, FlightInfo

def processDataByFile(fileName, flightDate):
    curDateTime =  time.localtime(time.time())
    
    queryDate = time.strftime('%Y-%m-%d', curDateTime)
    queryTime = time.strftime('%H:%M:%S', curDateTime)
    
    retList = qunar.analysis(fileName)
    
    db = DB('atp', 'atp', 'atp')
    conn = db.getConn()
    if not conn:
        print "connect db failed."
        return -1
    
    handler = FlightInfoHandler(conn)
    
    for rec in retList:
        flightInfo = FlightInfo(queryDate, queryTime, flightDate, rec)
        handler.insertOneRec(flightInfo)
        
    return 0

