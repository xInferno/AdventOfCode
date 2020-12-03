#!/usr/bin/python

import sys
from sys import argv

def isValid(a,b,c):
  if (a + b) > c and (a + c) > b and (b + c) > a: return 1
  else: return 0

script, infile = argv

valid = 0

with open(infile,'r') as inputfile:
  linelist = inputfile.readlines()

for z in range(0,len(linelist)):
    valid += isValid(int(linelist[z].split()[0]),int(linelist[z].split()[1]),int(linelist[z].split()[2]))

print("Number of valid triangles: " + str(valid))
