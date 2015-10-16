import sys
from custom.custom_airport import getCustomArrAirport, getCustomDepAirport
from search_simulate import workSimulateQunar

def main():
    if len(sys.argv) != 2:
        print "Usage: {} casperjs_script".format(sys.argv[0])
        return 1
    
    casperScript = sys.argv[1]
    depAirportList = getCustomDepAirport()
    arrAirportList = getCustomArrAirport()
    
    workSimulateQunar(casperScript, depAirportList, arrAirportList, 60, 5)

if __name__ == '__main__':
    main()