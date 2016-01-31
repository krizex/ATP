#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from analysis.lowest.result import ResultMap
from atp.dbc import DB

__author__ = 'David Qian'

"""
Created on 01/28/2016
@author: David Qian

"""


def analysis_lowest(dep_code, arr_code):
    result_map = ResultMap()
    db = DB('atp', 'atp', 'atp')
    conn = db.getConn()
    cursor = conn.cursor()
    cursor.execute("select * from FLIGHT_LOWEST_PRICE_INFO where dep_code='%s' and arr_code='%s'" % (dep_code, arr_code))
    # print cursor.rowcount
    while True:
        result = cursor.fetchone()
        # print result
        if not result:
            break

        query_date = result[1]
        dep_date = result[5]
        price = result[11]
        result_map.add((dep_date - query_date).days, price)

    print 'FROM:%s    TO:%s' % (dep_code, arr_code)
    result_map.analysis()


def print_usage():
    print """Usage:
    python -m analysis.lowest.lowest_price <FROM> <TO>
    """

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage()
        exit(1)

    from_code = sys.argv[1]
    to_code = sys.argv[2]
    analysis_lowest(from_code, to_code)


