# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from airport import getAllAirport
import datetime
from flight_info import FlightLowestPriceInfoHandler, FlightLowestPriceInfo
import time

class QunarLowest:
    def __init__(self, conn, allAirports):
        self.conn = conn
        self.allAirports = allAirports
        self.dbHandle = FlightLowestPriceInfoHandler(conn)
        
    def crawlAllAirlines(self):
        for i in range(len(self.allAirports)):
            dep = self.allAirports[i]
            for j in range(len(self.allAirports)):
                if i == j:
                    continue
                
                arr = self.allAirports[j]
                
                startDate = datetime.datetime.today() + datetime.timedelta(days=1)
                self.crawlOneAirline(dep, arr, startDate.strftime("%Y-%m-%d"), 60)
                return 1
    
    def crawlOneAirline(self, depInfo, arrInfo, startDate, dateRange):
        curDateTime =  time.localtime(time.time())
        queryDate = time.strftime('%Y-%m-%d', curDateTime)
        queryTime = time.strftime('%H:%M:%S', curDateTime)
        urlBase = "http://flight.qunar.com/twell/flight/farecast.jsp?departureCity={}&arrivalCity={}&nextNDays=0&departureDate={}&searchType=OnewayFlight&searchLangs=zh&locale=zh&serverIP=twell4&allowOld=true&queryID=127.0.0.1%3A1c1ea29%3A113aed2be0b%3A-7bfb&dayNum={}&pageNum=0"
        url = urlBase.format(depInfo[1], arrInfo[1], startDate, dateRange)
        r = requests.get(url)
        if r.status_code != 200:
            return 1
        
        print url
    #     print r.text
        bs = BeautifulSoup(r.text, 'lxml-xml')
    #     print bs.ResultData
        resultData = bs.find('ResultData')
        for airline in resultData.children:
            if airline.name == 'lowestPrice':
                d = airline.attrs
                info = FlightLowestPriceInfo(queryDate, queryTime, depInfo[0], arrInfo[0], (d['date'], d['code'], d['depTime'], d['arrTime'], d['carrier'], d['vendorName'], d['price']))
                print info.asRec()
                self.dbHandle.insertOneRec(info)
                
if __name__ == '__main__':
    q = QunarLowest(None, getAllAirport())
    q.crawlAllAirlines()
        