# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from airport import getAllAirport
import datetime
from flight_info import FlightLowestPriceInfoHandler, FlightLowestPriceInfo
import time
from dbc import DB
from time_limit_execute import timeLimitExecute
from logger import L
from errcode import ER_SUCC, ER_REQUEST_TIMEOUT, ER_RESPONSE_FAIL

class QunarLowest:
    def __init__(self, conn, allAirports, dateRange):
        self.conn = conn
        self.allAirports = allAirports
        self.dbHandle = FlightLowestPriceInfoHandler(conn)
        self.lstFailAirline = []
        self.dateRange = dateRange
        
    def crawlAllAirlinesWithRetry(self, retryTime):    
        self.crawlAllAirlines()
        
        lstCur = self.lstFailAirline
        lstNext = []
        for i in range(1, retryTime + 1):
            if len(lstCur) == 0:
                return ER_SUCC
            
            for it in lstCur:
                L.info("retry[{}] {} -> {}", i, it[0][0], it[1][0])
                startDate = datetime.datetime.today() + datetime.timedelta(days=1)
                if ER_SUCC != self.crawlOneAirline(it[0], it[1], startDate):
                    lstNext.append(it)
                    
            lstCur = lstNext
            
        for it in lstCur:
            L.error("{} -> {} retry {} times failed", it[0][0], it[1][0], retryTime)
        
    def crawlAllAirlines(self):
        for i in range(len(self.allAirports)):
            dep = self.allAirports[i]
            for j in range(len(self.allAirports)):
                if i == j:
                    continue
                
                arr = self.allAirports[j]
                
                startDate = datetime.datetime.today() + datetime.timedelta(days=1)
                if ER_SUCC != self.crawlOneAirline(dep, arr, startDate.strftime("%Y-%m-%d")):
                    self.lstFailAirline.append((dep, arr))
                
    @timeLimitExecute(20)
    def crawlOneAirline(self, depInfo, arrInfo, startDate):
        curDateTime =  time.localtime(time.time())
        queryDate = time.strftime('%Y-%m-%d', curDateTime)
        queryTime = time.strftime('%H:%M:%S', curDateTime)
        urlBase = "http://flight.qunar.com/twell/flight/farecast.jsp?departureCity={}&arrivalCity={}&nextNDays=0&departureDate={}&searchType=OnewayFlight&searchLangs=zh&locale=zh&serverIP=twell4&allowOld=true&queryID=127.0.0.1%3A1c1ea29%3A113aed2be0b%3A-7bfb&dayNum={}&pageNum=0"
        url = urlBase.format(depInfo[1], arrInfo[1], startDate, self.dateRange)
#         print url
        try:
            r = requests.get(url, timeout=10)
        except:
            L.error("{} -> {} timeout, url={}", depInfo[0], arrInfo[0], url)
            return ER_REQUEST_TIMEOUT
            
        if r.status_code != 200:
            L.error("{} -> {} failed, url={}", depInfo[0], arrInfo[0], url)
            return ER_RESPONSE_FAIL
        
        L.info("{} -> {}", depInfo[0], arrInfo[0])
        bs = BeautifulSoup(r.text, 'lxml-xml')
        resultData = bs.find('ResultData')
        for airline in resultData.children:
            if airline.name == 'lowestPrice':
                d = airline.attrs
                allAttrs = ('date', 'code', 'depTime', 'arrTime', 'carrier', 'vendorName', 'price')
                attrOK = True
                for attr in allAttrs:
                    if attr not in d:
                        attrOK = False
                        break
                if not attrOK:
                    continue        
                    
                info = FlightLowestPriceInfo(queryDate, queryTime, depInfo[0], arrInfo[0], [d[x] for x in allAttrs])
#                 print info.asRec()
                self.dbHandle.insertOneRec(info)
                
        return ER_SUCC
                
if __name__ == '__main__':
    db = DB('atp', 'atp', 'atp')
    q = QunarLowest(db.getConn(), getAllAirport(), 60)
    q.crawlAllAirlinesWithRetry(5)
