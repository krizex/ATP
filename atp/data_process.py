from atp import qunar
import time
from atp.dbc import DB
from atp.flight_info import FlightInfoHandler, FlightInfo
from atp.logger import L
from atp.errcode import ER_CONN_DB_FAILED, ER_SUCC

g_db = DB('atp', 'atp', 'atp')

def processDataByFile(fileName, depDate, depCode, arrCode):
    curDateTime = time.localtime(time.time())
    
    queryDate = time.strftime('%Y-%m-%d', curDateTime)
    queryTime = time.strftime('%H:%M:%S', curDateTime)
    
    retList = qunar.analysis(fileName)
    if not retList:
        L.error("Not found airline")

    global g_db
    conn = g_db.getConn()
    if not conn:
        L.error("connect db failed.")
        return ER_CONN_DB_FAILED
    
    handler = FlightInfoHandler(conn)
    
    for rec in retList:
        flightInfo = FlightInfo(queryDate, queryTime, depDate, depCode, arrCode, rec)
        handler.insertOneRec(flightInfo)
        
    return ER_SUCC

