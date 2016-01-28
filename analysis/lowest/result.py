#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'David Qian'

"""
Created on 01/28/2016
@author: David Qian

"""


class ResultMap(object):
    def __init__(self):
        self.result = {}

    def add(self, date_delta, price):
        if date_delta in self.result:
            m = self.result[date_delta]
            m[0] += price
            m[1] += 1
        else:
            m = [price, 1]
            self.result[date_delta] = m

    def analysis(self):
        print 'delta_day    avg_price    query_time'
        for i in range(60):
            if i not in self.result:
                continue
            m = self.result[i]
            print '{}    {}    {}'.format(i, m[0]/m[1], m[1])

