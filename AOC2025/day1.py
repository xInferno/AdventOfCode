#!/usr/bin/env python3

input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile if not x.strip().startswith("#") or x.strip().startswith(" ")]
    return infile

def p1(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug

    cursor = 50
    zeros = 0
    for i in given:
        if i[0] == 'L':
            cursor-= int(i[1:])
            while cursor < 0:
                cursor += 100
        elif i[0] == 'R':
            cursor+= int(i[1:])
            while cursor > 99:
                cursor -= 100
        else:
            return "Improperly formatted input, please recheck input file"
        if cursor == 0:
            zeros += 1

    return str(zeros)

# This was a brute force method of figuring out the answer to debug my original slightly-less-naive algorithm
def p2_naive(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    cursor = 50
    zeros = 0
    for i in given:
            count = int(i[1:])
            while count > 0:
                if i[0] == "L":
                    cursor -= 1
                elif i[0] == "R":
                    cursor += 1
                count -= 1
                if cursor == -1:
                    cursor = 99
                if cursor == 100:
                    cursor = 0
                if cursor == 0:
                    zeros += 1

    return str(zeros)


def p2(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug
    cursor = 50
    zeros = 0
    for i in given:
        cursor_initial = cursor
        if i[0] == 'L':
            cursor-= int(i[1:])
            while cursor <= 0:
                if cursor == 0:
                    # We landed on zero, need to handle separately to avoid a loop
                    zeros += 1
                    break
                cursor += 100
                if cursor_initial == 0:
                    # We started at zero, we didn't *cross* zero
                    cursor_initial = -1
                    continue
                else:
                    zeros += 1
        elif i[0] == 'R':
            cursor+= int(i[1:])
            while cursor > 99:
                cursor -= 100
                zeros += 1
        else:
            return "Improperly formatted input, please recheck input file"

    return str(zeros)


def main():
    given = process(input_file)       
    print("P1: " + p1(given, 0))
    #print("P2 Naive: " + p2_naive(given, 0))
    print("P2: " + p2(given, 0))

if __name__ == '__main__':
    main()
