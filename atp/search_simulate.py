import datetime
import commands
from data_process import processDataByFile
from logger import L
from errcode import ER_SUCC

def searchRange(casperScript, dep, arr, dateRange, retryTimes):
    depTime = datetime.datetime.today()
    d = datetime.timedelta(days=1)
    for i in range(dateRange):
        depTime = depTime + d
        ret = ER_SUCC
        for j in range(retryTimes):
            ret = searchOne(casperScript, dep, arr, depTime.strftime("%Y-%m-%d"))
            if ret == ER_SUCC:
                L.info("{} -> {}  {}", dep[0], arr[0], depTime.strftime("%Y-%m-%d"))
                break
        
        if ER_SUCC != ret:
            L.error("retry {} times, {} -> {}  {} failed", retryTimes, dep[0], arr[0], depTime.strftime("%Y-%m-%d"))

    
#dep = (depCode, depAirport)
def searchOne(casperScript, dep, arr, depDate):
    cmd = "casperjs '{}' '{}' '{}' '{}' '{}' '{}'".format(casperScript, dep[0], dep[1], arr[0], arr[1], depDate)
    ret, out = commands.getstatusoutput(cmd)
    if ret != ER_SUCC:
#         L.error("Execute command[{}] failed, errCode: {}, errMsg: {}".format(cmd, ret, out))
        L.error("Execute command[{}] failed, errCode: {}, errMsg:{}", cmd, ret, out)
        return ret
    
#     L.debug("Execute command[{}] succeed, Msg: {}".format(cmd, out))
    L.debug("Execute command[{}] succeed", cmd)
    ret = processDataByFile("/tmp/searchResult.html", depDate, dep[0], arr[0])
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