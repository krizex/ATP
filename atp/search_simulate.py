import datetime
from errcode import *
import commands
from data_process import processDataByFile
import sys

def searchRange(casperScript, dep, arr, dateRange, retryTimes):
    depTime = datetime.datetime.today()
    d = datetime.timedelta(days=1)
    for i in range(dateRange):
        depTime = depTime + d
        ret = ER_SUCC
        for j in range(retryTimes):
            ret = searchOne(casperScript, dep, arr, depTime.strftime("%Y-%m-%d"))
            if ret == ER_SUCC:
                print "[{}] {} -> {} : {}".format(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), dep[0], arr[0], depTime.strftime("%Y-%m-%d"))
                break
        
        if ER_SUCC != ret:
            print "[{}] retry {} times, {} -> {} : {} failed".format(retryTimes, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), dep[0], arr[0], depTime.strftime("%Y-%m-%d"))

    
#dep = (depCode, depAirport)
def searchOne(casperScript, dep, arr, depDate):
    cmd = "casperjs '{}' '{}' '{}' '{}' '{}' '{}'".format(casperScript, dep[0], dep[1], arr[0], arr[1], depDate)
    ret, out = commands.getstatusoutput(cmd)
    if ret != ER_SUCC:
        print "Execute command[{}] failed, errCode: {}, errMsg: {}".format(cmd, ret, out)
        return ret
    
#     print "Execute command[{}] succeed, Msg: {}".format(cmd, out)
    ret = processDataByFile("/tmp/searchResult.html", depDate)
    return ret

def workSimulateQunar(casperScript, depAirportList, arrAirportList, dateRange=60, retryTimes=5):
    for dep in depAirportList:
        for arr in arrAirportList:
            if dep[0] == arr[0]:
                continue
            
            #go
            searchRange(casperScript, dep, arr, dateRange, retryTimes)
            #back
            searchRange(casperScript, arr, dep, dateRange, retryTimes)
    
            
    return ER_SUCC