#!/usr/bin/env python
import os
import sys
import datetime
from atp.errcode import ER_CONN_DB_FAILED
from atp.flight_info import FlightInfoHandler, FlightLowestPriceInfoHandler
from atp.data_process import g_db
from atp.logger import L

__author__ = 'QianYang'

def usage():
    print '''Usage:
    {} table_name [duration]
    '''.format(os.path.basename(sys.argv[0]))

def statis4FlightInfo(duration):
    conn = g_db.getConn()
    if not conn:
        L.error("connect db failed.")
        return ER_CONN_DB_FAILED

    handler = FlightInfoHandler(conn)
    print "FlightInfo:"
    for i in range(duration, -1, -1):
        queryDate = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        recNum = handler.getRecordNum(query_date=queryDate)
        print "{} : {}".format(queryDate, recNum)

def statis4FlightLowestPriceInfo(duration):
    conn = g_db.getConn()
    if not conn:
        L.error("connect db failed.")
        return ER_CONN_DB_FAILED

    handler = FlightLowestPriceInfoHandler(conn)
    print "FlightLowestPriceInfo:"
    for i in range(duration, -1, -1):
        queryDate = (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        recNum = handler.getRecordNum(query_date=queryDate)
        print "{} : {}".format(queryDate, recNum)

def main():
    if len(sys.argv) < 2:
        usage()
        return

    tblName = sys.argv[1]
    try:
        duration = int(sys.argv[2])
    except:
        duration = 60

    if tblName == "FlightInfo":
        statis4FlightInfo(duration)
    elif tblName == "FlightLowestPriceInfo":
        statis4FlightLowestPriceInfo(duration)
    else:
        print "Invalid table name."


if __name__ == '__main__':
    main()