#!/usr/bin/env python3

#input_file = 'inputs/day2_sample'
input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    # This allows me to comment out portions of the input file to iteratively test on subsets of data
    infile = [x.strip().split(',') for x in infile if not x.strip().startswith("#") or x.strip().startswith(" ")]

    return infile

def p1(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug
    invalid = []
    for i in given:
        for j in i:
            rang = j.split('-') 
            cursor = int(rang[0])
            last = int(rang[1])
            while cursor <= last:
                cursor_string = str(cursor)
                if len(cursor_string) % 2 != 0: # odd number of digits, cannot be a repeating number
                    cursor += 1
                    continue
                # split the cursor in half, check if both sides are equal
                front = int(cursor_string[0:int(len(cursor_string)/2)])
                back = int(cursor_string[int(len(cursor_string)/2):int(len(cursor_string))])
                if front == back:
                    invalid.append(cursor) 
                cursor += 1

    debug_print(invalid)
    sum = 0
    for x in invalid:
        sum += int(x)

    return str(sum)
def p2(given, debug):
    # hm. naive solution is probably not gonna work here. I wonder if I can do this with regex.
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug
    invalid = []
    for i in given:
        for j in i:
            rang = j.split('-') 
            cursor = int(rang[0])
            last = int(rang[1])
            while cursor <= last:
                cursor += 1

    return "TBD"

def main():
    debug1, debug2 = 0, 1
    given = process(input_file)       
    print("P1: " + p1(given, debug1))
    print("P2: " + p2(given, debug2))

if __name__ == '__main__':
    main()
