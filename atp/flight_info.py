
class FlightInfo:
    def __init__(self, queryDate, queryTime, flightDate, rec):
        #flightNo, depTime, depAirport, arrTime, arrAirport, elapsedTime, ptyRate, delayTime, ticketPrice)
        self.queryDate = queryDate
        self.queryTime = queryTime
        self.flightDate = flightDate
        self.flightNo = rec[0].encode('utf8')
        self.depTime = rec[1].encode('utf8')
        self.depAirport = rec[2].encode('utf8')
        self.arrTime = rec[3].encode('utf8')
        self.arrAirport = rec[4].encode('utf8')
        self.elapsedTime = rec[5].encode('utf8')
        self.ptyRate = rec[6].encode('utf8')
        self.delayTime = rec[7].encode('utf8')
        self.ticketPrice = rec[8].encode('utf8')
        
    def asRec(self):
        return (self.queryDate, self.queryTime, self.flightDate, self.flightNo, self.depTime, self.depAirport,
                self.arrTime, self.arrAirport, self.elapsedTime, self.ptyRate, self.delayTime, self.ticketPrice)
        
class FlightInfoHandler:
    def __init__(self, conn):
        self.conn = conn
    
    INSERT_SQL = "INSERT INTO FLIGHT_INFO (query_date, query_time, flight_date, flight_number, \
                  dep_time, dep_airport, arr_time, arr_airport, elapsed_time, punctuality_rate, \
                  delay_time, ticket_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                  
    def insertOneRec(self, flightInfo):
        cursor = self.conn.cursor()
        try:
            cursor.execute(self.INSERT_SQL, flightInfo.asRec())
            self.conn.commit()
        except:
            print "insert failed"
            self.conn.rollback()
            
        cursor.close()
            
