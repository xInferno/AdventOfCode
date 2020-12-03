#!/usr/bin/python
from sys import argv
import re

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

x = 0
y = 0
direct = 'n'
k = ''
with open(filename,'r') as inputfile:
  string = inputfile.read().replace(' ','')

for i in string:
  for j in i:
    if j == 'R':
      #print("Found an R, should read the next int")
      direct = point(direct, 2)
      print("Currently facing: " + direct)
    elif j == 'L':
      #print("Found an L, should read the next int")
      direct = point(direct, 1)
      print("Currently facing: " + direct)
    elif j == ',':
      #print("Found a comma, now's the time to do the operation")
      print("The current int is: " + k)
      if direct == 'n': y += int(k)
      elif direct == 's': y -= int(k)
      elif direct == 'e': x -= int(k)
      elif direct == 'w': x += int(k)
      else: print("error with function")
      print("Current x and y values: " + str(x) + ", " + str(y))
      k = ''
    else:
      #print("Found a character to be cat'd to an int")
      k += j


if direct == 'n': y += int(k)
elif direct == 's': y -= int(k)
elif direct == 'e': x -= int(k)
elif direct == 'w': x += int(k)
else: print("error with function")
print("Current x and y values: " + str(x) + ", " + str(y))

distance = abs(x) + abs(y)

print("Your distance from Easter Bunny HQ is: " + str(distance))
