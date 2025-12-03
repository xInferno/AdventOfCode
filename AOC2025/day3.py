#!/usr/bin/env python3

input_file = 'inputs/day3'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    # This allows me to comment out portions of the input file to iteratively test on subsets of data
    infile = [x.strip() for x in infile if not (x.strip().startswith("#") or x.strip().startswith(" ") or x.strip().startswith("/"))]
    return infile

def p1(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug

    digit1, digit2, total = 0, 0, 0
    indices = []
    for i in given:
        digit1 = max(i[:-1])

        for index, char in enumerate(i):
            if char == digit1:
                indices.append(index)
        
        if len(indices) == 1:
            digit2 = max(i[indices[0]+1:])
        elif max(i) == i[-1]:
            digit2 = i[-1]
        else:
            digit2 = digit1
        
        total += int(str(digit1) + str(digit2))
        
        indices = []
        

    return str(total)
def p2(given, debug):
    def debug_print(string):
        if DEBUG_PRINT:
            print(string)
    DEBUG_PRINT = debug

    total = 0
    for i in given:
        beg = 0
        # This is 11 to solve an off-by-one error that I haven't quite figured out
        end = len(i) - 11
        prev_beg = 0
        num_string = ""

        while len(num_string) < 12:
            j = i[beg:end]
            digit = max(j)
            indices = []
            for index, char in enumerate(j):
                if char == digit:
                    indices.append(index)
            num_string += str(j[indices[0]])
            prev_beg = beg
            beg = indices[0]+1 + prev_beg
            end += 1
            indicies = []

        total += int(num_string)

        num_string = ""
        
        
    return str(total)

def main():
    debug1, debug2 = 0, 0
    given = process(input_file)       
    print("P1: " + p1(given, debug1))
    print("P2: " + p2(given, debug2))

if __name__ == '__main__':
    main()
