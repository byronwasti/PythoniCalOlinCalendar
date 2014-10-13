import sys

# Setting up the program for writing the calendar files
class icalformat:
    #This is what formats all of the data into .ical
    def date(date):
        return 'writing files'
    def course(course):
        return ''
    def time(time):
        return ''

datain = open('testdata.txt','r') # Grabbing the data
dataout = open('testcalendar.ical','w') # The file to write data

numbevents = int(datain.readline(1)) #The number of events to make an ical for
print (numbevents) 


#Begining the writout of events
starter = ('BEGIN:VCALENDAR\n'
'VERSION:2.0\n'
'PRODID:-//bobbin v0.1//NONSGML iCal Writer//EN\n'
'CALSCALE:GREGORIAN\n'
'METHOD:PUBLISH\n')

dataout.write(starter)

for i in range(0,numbevents):
    
