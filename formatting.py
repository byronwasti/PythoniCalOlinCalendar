#import GetHTML
import sys
import datetime
import time

year = 2014
semester = 1

data = []
datain = open('testinput.txt')
numbcourse = int(datain.readline(1))
for i in range(0,numbcourse):

    data.append(datain.readline())

for i in range(0,numbcourse):
    

