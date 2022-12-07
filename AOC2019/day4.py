#!/usr/bin/env python3

input_file = 'inputs/day4'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given) -> list:
    digits = 6 
    decrease, double = 0, 0
    first, last = [int(x) for x in given[0].split("-")]
    partTwo = []

    for i in range(first, last+1):
        for j in range(0, digits-1):
            if int(str(i)[j]) > int(str(i)[j+1]):
                decrease = 1
                break # this number doesn't match, move to the next
            elif double:
                continue
            elif str(i)[j] == str(i)[j+1]:
                double = 1
                continue
        if not decrease and double:
            partTwo.append(i)
        double, decrease = 0, 0
        continue
    print("Number of possible passwords:",len(partTwo))
    return partTwo
def p2(given):
    answer = []
    # found a clever solution using count and a dictionary
    for i in given:
        tally = {}
        for j in str(i):
            tally[j] = str(i).count(j)
        if 2 in tally.values():
            answer.append(i)

    print("Number of possible passwords with stricter requirements:",len(answer))
    return

def main():
    given = process(input_file)       
    p2(p1(given))

if __name__ == '__main__':
    main()
