from atp.airport import getAllAirport
from atp.dbc import DB
from atp.qunar_lowest import QunarLowest

RECENT_DAY_RANGE = 60
RETRY_TIMES = 10

def workQunarLowest():
    db = DB('atp', 'atp', 'atp')
    q = QunarLowest(db.getConn(), getAllAirport(), RECENT_DAY_RANGE)
    q.crawlAllAirlinesWithRetry(RETRY_TIMES)
    
if __name__ == '__main__':
    workQunarLowest()
    
