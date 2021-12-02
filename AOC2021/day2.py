#!/usr/bin/env python3
import re

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    depth, pos = 0, 0
    for t in given:
        if t[0] == 'f':
            pos += int(t[-1])
        elif t[0] == 'd':
            depth += int(t[-1])
        elif t[0] == 'u':
            depth -= int(t[-1])
    print ("Depth is {}, Position is {}, answer is {}".format(depth,pos,depth*pos))
    return
def p2(given):
    depth, pos, aim = 0, 0, 0
    for t in given:
        if t[0] == 'f':
            pos += int(t[-1])
            depth += aim*int(t[-1])
        elif t[0] == 'd':
            aim += int(t[-1])
        elif t[0] == 'u':
            aim -= int(t[-1])
    print ("Depth is {}, Position is {}, answer is {}".format(depth,pos,depth*pos))
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
