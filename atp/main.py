import sys
from data_process import processDataByFile

if __name__ == '__main__':
    searchResultFile = '../test/searchResult.html'
    processDataByFile(searchResultFile, '2015-10-13')
    
if __name__ == '__main__1':
    searchResultFile = sys.argv[1]
    searchDate = sys.argv[2]
    processDataByFile(searchResultFile, searchDate)
