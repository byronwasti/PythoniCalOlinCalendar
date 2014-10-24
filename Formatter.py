import sys
import random
# Setting up the program for writing the calendar files
datain = open('testdata.txt','r') # Grabbing the data
import GetHTML

# Storing all of the data into a list called data
numbcourse = int(datain.readline(1))
data = []
for i in range(0,numbcourse* 3+1):
    data.append(datain.readline())
    #print(datain.readline())
    tmp = data[i]
    tmp = tmp.replace('\n','')
    data[i] = tmp
import pytz
#def SetEvent(course, time, location):
#    
#    timef = time.split(';',5)
#    locationf = location.split(';',5)
#
#    startevent = "BEGIN:VEVENT\n"
#    
#    cal = Calendar()
#    from datetime import datetime
#    cal.add('prodid','-//My calendar product//mxm.dk//')
#    cal.add('version','2.0')
#    
#    event = Event()
#    event.add('summary',course)
#    event.add('dstart',datetime(2014,
#    return event




dataout = open('testcalendar.ical','w') # The file to write data


#Begining the writout of events
starter = ('BEGIN:VCALENDAR\n'
'VERSION:2.0\n'
'PRODID:-//bobbin v0.1//NONSGML iCal Writer//EN\n'
'CALSCALE:GREGORIAN\n'
'METHOD:PUBLISH\n')

for i in range(0,numbcourse ):
    SetEvent(data[1+3*i],data[2+3*i],data[3+3*i])

dataout.write(starter)
