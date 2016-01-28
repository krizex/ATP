#!/usr/bin/env python
# -*- coding: utf-8 -*-
from analysis.lowest.result import ResultMap
from atp.dbc import DB

__author__ = 'David Qian'

"""
Created on 01/28/2016
@author: David Qian

"""


def analysis_lowest():
    result_map = ResultMap()
    db = DB('atp', 'atp', 'atp')
    conn = db.getConn()
    cursor = conn.cursor()
    cursor.execute('select * from FLIGHT_LOWEST_PRICE_INFO')
    print cursor.rowcount
    while True:
        result = cursor.fetchone()
        print result
        if not result:
            break

        query_date = result[0]
        dep_date = result[4]
        price = result[10]
        result_map.add((dep_date - query_date).days, price)
        break

    result_map.analysis()



if __name__ == '__main__':
    analysis_lowest()

