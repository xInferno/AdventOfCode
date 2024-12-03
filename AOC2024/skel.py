#!/usr/bin/env python3

input_file = 'inputs/day$'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    return "TBD"
def p2(given):
    return "TBD"

def main():
    given = process(input_file)       
    print("P1: " + p1(given))
    print("P2: " + p2(given))

if __name__ == '__main__':
    main()
