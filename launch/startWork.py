import commands
from airport import getAllAirport
import sys
from data_process import processDataByFile
import datetime

def searchRange(casperScript, dep, arr, dateRange):
    curTime = datetime.datetime.today()
    d = datetime.timedelta(days=1)
    for i in range(dateRange):
        curTime = curTime + d
        searchOne(casperScript, dep, arr, curTime.strftime("%Y-%m-%d"))
    
#dep = (depCode, depAirport)
def searchOne(casperScript, dep, arr, depDate):
    cmd = "casperjs '{}' '{}' '{}' '{}' '{}' '{}'".format(casperScript, dep[0], dep[1], arr[0], arr[1], depDate)
    ret, out = commands.getstatusoutput(cmd)
    if ret != 0:
        print "Execute command[{}] failed, errCode: {}, errMsg: {}".format(cmd, ret, out)
        return ret
    
    raise Exception()
    
    ret = processDataByFile("/tmp/searchResult.html", depDate)
    return ret

def main():
    if len(sys.argv) != 1:
        print "Usage: "
        return 1
    
    casperScript = sys.argv[1]
    
    arAirport = getAllAirport()
    for i in len(arAirport):
        dep = arAirport[i]
        for j in len(arAirport):
            if i == j:
                continue
            
            arr = arAirport[j]
            
            searchRange(casperScript, dep, arr, 60)
            
    
    return 0
            

if __name__ == '__main__':
    main()
    