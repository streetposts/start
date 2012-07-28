# Import functions

import time
import sqlite3 as sqlite

# Identiffication
print ('Streetposts 1.0 - by Joseph Wennechuk')

# Get stop number from user
stop = str(input ('Which stop were you interested in:'))
# Validate that stop exists.

# Query, and print stop Information from stops.
day = str.lower(time.strftime('%A'))
print 'The day of the week is:', day
time = time.strftime('%H:%M:%S')
print 'The time now is:', time
conn = sqlite.connect('/home/joseph/streetposts/streetposts.ca/grt.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM stops WHERE stop_id = '%s'" % stop)
stopInfo = c.fetchone()
print 'Latitude: %s Longitude: %s Stop Location: %s'  % (stopInfo[0], stopInfo[2], stopInfo[5])
c = conn.cursor()
print  time, stop, day
query = "SELECT DISTINCT trips.route_id, trips.trip_headsign, stop_times.departure_time FROM trips INNER JOIN stop_times ON trips.trip_id = stop_times.trip_id WHERE departure_time >'" + time +"' AND stop_id = '" + stop + "' AND trips.trip_id IN (SELECT trips.trip_id FROM trips WHERE trips.service_id IN (SELECT  calendar.service_id FROM calendar WHERE  " + day + "= '1')) ORDER BY departure_time LIMIT 10"
c.execute(query)
rows = c.fetchall()
for row in rows: 
   print row[0],row[1], row[2]
conn.close






