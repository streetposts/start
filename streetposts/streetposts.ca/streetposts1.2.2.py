import time
import sqlite3 as sqlite
from twilio.rest import TwilioRestClient
account = "AC961332ac43d2c29d9bdc9e6d105046b6"
token = "7c483f82958feeabef1257b9a922d7c7"
# Identiffication
print ('Streetposts 1.0 - by Joseph Wennechuk')

# Get stop number from user
def getStop():
  stop = str(input ('Which stop were you interested in:'))
# Validate that stop exists.
  return stop
#Get phone number
def getPhoneNumber():
  phoneNumber = str( input ('phone number please:'))
  return(phoneNumber)

#Get day of the week ofr query
def getDay():
  day = str.lower(time.strftime('%A'))
  return(day) 

def connectSQL():
  conn = sqlite.connect('/home/joseph/streetposts/streetposts.ca/grt.sqlite') 
  return(conn) 

def getNow():
  now = time.strftime('%H:%M:%S')
  return(now)

def locationInformation():
  conn = connectSQL()
  c = conn.cursor()
  c.execute("SELECT * FROM stops WHERE stop_id = '%s'" % stop)
  row = c.fetchone()
  location = row[5],row[0],row[2]
  c.close()
  return(location)

def buildQuery(time, stop, day, date):
  query = "SELECT DISTINCT trips.route_id, trips.trip_headsign, stop_times.departure_time FROM trips INNER JOIN stop_times ON trips.trip_id = stop_times.trip_id WHERE departure_time >'" + now +"' AND stop_id = '" + stop + "' AND trips.trip_id IN (SELECT trips.trip_id FROM trips WHERE trips.service_id IN (SELECT  calendar.service_id FROM calendar WHERE  " + day + "= '1' AND end_date >'" + date + "')) ORDER BY departure_time LIMIT 10"
  return(query)

def selectQuery(query):
  conn = connectSQL()
  c = conn.cursor()
  c.execute(query)
  result = c.fetchall()
  c.close()
  return(result)
  
def printQuery(query):
  for row in query: 
    print row[0], row[1], row[2]
  return()

def dateId():
  return time.strftime('%Y%m%d')

date = dateId()
stop = getStop()
phoneNumber = getPhoneNumber()
day = getDay()
conn = connectSQL()
now = getNow()
location = locationInformation()
print ('Location: %s Latitude: %s Longitude: %s' % (location[0],location[1],location[2])) 
query = buildQuery(now, stop, day, date)
result = selectQuery(query)
printQuery(result)
client = TwilioRestClient(account, token)
message = client.sms.messages.create(to="+12266006139", from_="+15199005326",
                                     body="Hello there!")
exit()




# Query, and print stop Information from stops.
#print 'The day of the week is:', day
#print 'The time now is:', now







