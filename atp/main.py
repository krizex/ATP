import sys
from data_process import processDataByFile

if __name__ == '__main__':
    searchResultFile = sys.argv[1]
    processDataByFile(searchResultFile)
