import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    

class SzAirline:
    def __init__(self):
        pass
    
    def getData(self):
        r = requests.get("http://api.qunar.com/zh_one.jcp?lane=NKG-DLC")
#         print r.text
        root = ET.fromstring(r.content)
        for airline in root:
            print airline.tag, airline.attrib
            for line in airline:
                print line.tag, line.attrib