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

    digit1, digit2, number, total = 0, 0, 0, 0
    indices = []
    for i in given:
        # Figure out the max integer in the list, not inclusive of the final number
        digit1 = max(i[:-1])

        # figure out all positions of the max digit in the list
        for index, char in enumerate(i):
            if char == digit1:
                indices.append(index)
        
        # If there's only one place where the largest number exists, find the largest number of the subset
        if len(indices) == 1:
            digit2 = max(i[indices[0]+1:])
        # If the largest digit exists at the end, it must be the second digit
        elif max(i) == i[-1]:
            digit2 = i[-1]
        # Otherwise the largest digit is duplicated and thus must be both the first and second digits
        else:
            digit2 = digit1
        
        # Create the integer representation of the string and add it to the list
        number = int(str(digit1) + str(digit2))
        total += number

            
        
        # clear the list of indices after every line
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
            digit1 = max(j)
            indices_d1 = []
            for index, char in enumerate(j):
                if char == digit1:
                    indices_d1.append(index)
            num_string += str(j[indices_d1[0]])
            prev_beg = beg
            beg = indices_d1[0]+1 + prev_beg
            end += 1
            indicies_d1 = []

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
