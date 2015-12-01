# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from atp.logger import L

def analysis(fileName):
    retList = []
    with open(fileName) as f:
        s = BeautifulSoup(f, 'html.parser')
        sub = s.find(class_='e_fly_lst')
        if not sub:
            return None
        for airline in sub.children:
            if 'class' in airline.attrs and len(airline['class']) == 1 and airline['class'][0] == u'avt-column':
                print airline
                L.debug("{}", airline['id'])
                info = airline.contents[0].contents
                L.debug("{}", info)
                try:
                    flightNo = getFlightNumber(info[1])
                    depTime, depAirport = getDepartureTimeAirport(info[2])
                    elapsedTime = getElapsedTime(info[3])
                    arrTime, arrAirport = getArriveTimeAirport(info[4])
                    ptyRate, delayTime = getPunctualityRateDelayTime(info[5])
                    ticketPrice = getTicketPrice(info[6])
                except:
                    L.warning("Get info from airline failed. content = {}", airline)
                    continue
                
                rec = (flightNo, depTime, depAirport, arrTime, arrAirport, elapsedTime, ptyRate, delayTime, ticketPrice)
                retList.append(rec)
    return retList
                
#<div class="c1"><div class="vlc-wp"><div class="vlc-ref"></div><div class="vlc-con"><div class="air-wp"><div class="air-row"><div class="a-logo"><img width="24" height="24" title="中国深圳航空公司" alt="中国深圳航空公司" src="http://simg1.qunarzz.com/site/images/airlines/ZH.gif"></div></div><div class="air-row"><div class="a-name">深圳航空</div><div class="a-model"><span class="n">ZH4962</span><span class="n">波音737(中)</span><a class="p-tip-trigger n n-gx"><div class="n-gx-tit">共享</div><div class="p-tips-cont"><div class="p-tips-wrap"><div class="p-tips-arr p-tips-arr-t"><p class="arr-o">◆</p><p class="arr-i">◆</p></div><div class="p-tips-content"><p><span class="bold">主飞航班:</span>中国国航CA8958</p></div></div></div></a></div></div></div></div></div></div>            
def getFlightNumber(node):
    flightNumber = node.find(class_='a-model').contents[0].string
#     L.debug("{}", flightNumber)
    return flightNumber
    
#<div class="c2"><div class="a-dep-time">14:35</div>    <div class="a-dep-airport">禄口机场</div></div>
def getDepartureTimeAirport(node):
    depTime = node.find(class_='a-dep-time').string
    depAirport = node.find(class_='a-dep-airport').string
#     L.debug("{}, {}", depTime, depAirport)
    return (depTime, depAirport)

#<div class="c3"><div class="bg-tm"><p class="bg"></p></div><div class="a-zh-wp"><div class="a-tm-be">1小时45分钟</div></div></div>
def getElapsedTime(node):
    elapsedTime = node.find(class_='a-tm-be').string
#     L.debug("{}", elapsedTime)
    return elapsedTime

#<div class="c4"><div class="a-arr-time">16:20</div>    <div class="a-arr-airport">周水子机场</div></div>
def getArriveTimeAirport(node):
    arrTime = node.find(class_='a-arr-time').string
    arrAirport = node.find(class_='a-arr-airport').string
#     L.debug("{}, {}", arrTime, arrAirport)
    return (arrTime, arrAirport)

#<div class="c5"><div class="vlc-wp"><div class="vlc-ref"></div><div class="vlc-con"><div class="a-pty"><p class="a-pty-mint">77%</p><p class="a-pty-mint">22分钟</p></div></div></div></div>
def getPunctualityRateDelayTime(node):
    node = node.find(class_='a-pty')
    try:
        ptyRate = node.contents[0].string
    except:
        ptyRate = ''
    
    try:
        ptyDelay = node.contents[1].string
    except:
        ptyDelay = ''
    
#     L.debug("{}, {}", ptyRate, ptyDelay)
    return (ptyRate, ptyDelay)
    
# <div class="c6"><div class="vlc-wp"><div class="vlc-ref"></div><div class="vlc-con" id="recommandWrapperXI36"><a class="a-rec p-tip-trigger" hidefocus="on" id="reWrBtnXI36" data-evtdataid="XI36"><span class="rec-name">商旅优选</span><span class="rcpr"><i class="rmb">¥</i>392</span><div class="p-tips-cont" id="reCommOtaTipXI36"><div class="p-tips-wrap"><div class="p-tips-arr p-tips-arr-t"><p class="arr-o">◆</p><p class="arr-i">◆</p></div><div class="p-tips-content"><p><span class="bold">商旅优选</span></p><p>出票迅速：支付后极速出票</p><p>报销无忧：起飞后可邮寄行程单</p><p>服务优先：7*24小时全天候服务</p></div></div></div></a></div></div></div>
def getTicketPrice(node):
    price = node.find(class_='rcpr').contents[1]
#     L.debug("{}", price)
    return price
        

if __name__ == '__main__':
    analysis('../.testFile/searchResult.html')