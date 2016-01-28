#!/usr/bin/env python
# -*- coding: utf-8 -*-
from atp.dbc import DB

__author__ = 'David Qian'

"""
Created on 01/28/2016
@author: David Qian

"""


def analysis_lowest():
    db = DB('atp', 'atp', 'atp')
    conn = db.getConn()
    cursor = conn.cursor()
    cursor.execute('select * from FLIGHT_LOWEST_PRICE_INFO')
    while True:
        result = cursor.fetchone()
        if not result:
            break

        print result
        break


if __name__ == '__main__':
    analysis_lowest()

