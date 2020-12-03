#!/usr/bin/python
import re
import sys
from sys import argv
def point(direct, lr):
  if direct == 'n':
    if lr == 1:
      direct = 'w'
    else:
      direct = 'e'

  elif direct == 's':
    if lr == 1:
      direct = 'e'
    else:
      direct = 'w'

  elif direct == 'e':
    if lr == 1:
      direct = 'n'
    else:
      direct = 's'

  elif direct == 'w':
    if lr == 1:
      direct = 's'
    else:
      direct = 'n'

  else:
      direct = 'f'

  return direct

script, filename = argv
dis = -2
x = 0
y = 0
pos=[x, y]
posstack=[pos[:]]
found = 0
direct = 'n'
k = ''
with open(filename,'r') as inputfile:
  string = inputfile.read().replace(' ','')

for i in string:
  for j in i:
    if j == 'R':
    #  print("Found an R, should read the next int")
      direct = point(direct, 2)
     # print("Currently facing: " + direct)
    elif j == 'L':
      #print("Found an L, should read the next int")
      direct = point(direct, 1)
      #print("Currently facing: " + direct)
    elif j == ',':
      #print("Found a comma, now's the time to do the operation")
      #print("The current int is: " + k)
      if direct == 'n':
       # print("hit n")
        dis = int(k)
        while dis != 0:
          y += 1
          pos = [x, y]
          if pos in posstack and found != 1:
            print("Easter Bunny HQ Distance: " +(str(abs(x)+abs(y))))
            found = 1
          else:
            posstack.append(pos[:])
            dis -= 1
            #print("Position: " + str(x) + "," + str(y) + ", distance = " + str(dis))
      elif direct == 's': 
        dis = int(k)
        #print("Hit the dis setting block, dis is currently: " + str(dis))
        while dis != 0:
          y -= 1
          pos = [x, y]
          if pos in posstack and found != 1:
            print("Easter Bunny HQ Distance: " +(str(abs(x)+abs(y))))
            found = 1
          else:
            posstack.append(pos[:])
            #print("Printing it again: " + str(dis))
            dis -= 1
            #print("Position: " + str(x) + "," + str(y) + ", distance = " + str(dis))
      elif direct == 'e': 
        dis = int(k)
        while dis != 0:
          x += 1
          pos = [x, y]
          if pos in posstack and found != 1:
            print("Easter Bunny HQ Distance: " +(str(abs(x)+abs(y))))
            found = 1
          else:
            posstack.append(pos[:])  
            dis -= 1 
            #print("Position: " + str(x) + "," + str(y) + ", distance = " + str(dis))
      elif direct == 'w':
        dis = int(k)
        while dis != 0:
          x -= 1
          pos = [x, y]
          if pos in posstack and found != 1:
            print("Easter Bunny HQ Distance: " +(str(abs(x)+abs(y))))
            found = 1
          else:
            posstack.append(pos[:]) 
            dis -= 1
            #print("Position: " + str(x) + "," + str(y) + ", distance = " + str(dis))
      else: print("error with function")
      #print("Current x and y values: " + str(x) + ", " + str(y))
      k = ''
    else:
      #print("Found a character to be cat'd to an int")
      k += j


dis = int(k)
while dis != 0:
  y += 1
  pos = [x, y]
  if pos in posstack and found != 1:
    print("Easter Bunny HQ Distance: " +(str(abs(x)+abs(y))))
    found = 1
  else:
    posstack.append(pos[:]) 
    dis -= 1
 #   print("Position: " + str(x) + "," + str(y) + ", distance = " + str(dis))
