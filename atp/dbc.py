import MySQLdb

class DB:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self.connected = False
        self.conn = None
        
    def getConn(self):
        if self.connected == True:
            return self.conn
        
        try:
            self.conn = MySQLdb.connect(self.host, self.user, self.password, self.db)
            self.connected = True
        except:
            self.conn = None
            
        return self.conn
