#!/usr/bin/env python3
import re

input_file = 'inputs/day$'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    print("Part 1 TBD")
    return
def p2(given):
    print("Part 2 TBD")
    return

def main():
    given = process(input_file)       
    #p1(given)
    #p2(given)

if __name__ == '__main__':
    main()
