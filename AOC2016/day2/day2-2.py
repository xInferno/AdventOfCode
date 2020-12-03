#!/usr/bin/python

import sys
from sys import argv

def number(x,y):
  if x == 0 and y == 2: return 1
  elif x == -1 and y == 1: return 2
  elif x == 0 and y == 1: return 3 
  elif x == 1 and y == 1: return 4
  elif x == -2 and y == 0: return 5
  elif x == -1 and y == 0: return 6
  elif x == 0 and y == 0: return 7
  elif x == 1 and y == 0: return 8
  elif x == 2 and y == 0: return 9
  elif x == -1 and y == -1: return 'A'
  elif x == 0 and y == -1: return 'B'
  elif x == 1 and y == -1: return 'C'
  elif x == 0 and y == -2: return 'D'
  else: return 0
  

x = -2
y = 0

script, filename = argv

with open(filename,'r') as inputfile:
  linelist = inputfile.readlines()
  count = len(linelist) 

for z in range(0,count):
  string = linelist[z]
  for i in string:
    #print("start coordinates: " + str(x) + "," + str(y))
    if i == 'U':
      if y == 2 or (y == 1 and (x == 1 or x == -1)) or (x == -2 or x == 2):
    #    print("y at max, continuing")
        continue
      else:
        y += 1
    #    print("new coordinates after U" + str(x) + "," + str(y))
    elif i == 'D':
      if y == -2 or (y == -1 and (x == 1 or x == -1)) or (x == -2 or x == 2):
    #    print("y at min, continuing")
        continue
      else:
        y -= 1
    #    print("new coordinates after D" + str(x) + "," + str(y))
    elif i == 'L':
      if x == -2 or (x == -1 and (y == 1 or y == -1)) or (y == 2 or y == -2):
    #    print("x at min, continuing")
        continue
      else:
        x -= 1
    #    print("new coordinates after L" + str(x) + "," + str(y))
    elif i == 'R':
      if x == 2 or (x == 1 and (y == 1 or y == -1)) or (y == 2 or y == -2):
    #    print("x at max, continuing")
        continue
      else:
        x += 1
    #    print("new coordinates after R" + str(x) + "," + str(y))
    else:
       break
  print("Final number: " + str(number(x,y)))  
