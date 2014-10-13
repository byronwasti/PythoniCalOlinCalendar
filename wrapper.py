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

for i in range(0,numbevents):
    



test = icalformat.date()
print (test)
dataout.write(test)
    
