from airport import getAllAirport
from dbc import DB
from qunar_lowest import QunarLowest
from errcode import *

def workQunarLowest():
    db = DB('atp', 'atp', 'atp')
    q = QunarLowest(db.getConn(), getAllAirport(), 60)
    q.crawlAllAirlinesWithRetry(5)
    
if __name__ == '__main__':
    workQunarLowest()
    
