#!/usr/bin/env python3

input_file = 'inputs/day$'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    # This allows me to comment out portions of the input file to iteratively test on subsets of data
    infile = [x.strip() for x in infile if not x.strip().startswith("#") or x.strip().startswith(" ")]
    return infile

def p1(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug

    return "TBD"
def p2(given):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug

    return "TBD"

def main():
    given = process(input_file)       
    print("P1: " + p1(given, debug))
    print("P2: " + p2(given, debug))

if __name__ == '__main__':
    main()
