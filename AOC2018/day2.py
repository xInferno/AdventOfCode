#!/usr/bin/env python3

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    answer = 0
    twice, thrice, found2, found3 = 0, 0, 0, 0
    for i in given:
        print("==========Checking string ", i, "=========")
        for j in i:
            print("Checking char ", j)
            if i.count(j) == 2:
                print("Char",j,"found twice")
                if found2:
                    print("Already counted this or another character twice, continuing")
                    continue
                else:
                    found2 = 1
                    twice += 1
            if i.count(j) == 3:
                print("Char",j,"found three times")
                if found3:
                    print("Already counted this or another character three times, continuing")
                else:
                    found3 = 1
                    thrice += 1
        found2, found3 = 0, 0
    print("Twice: ", twice, ", thrice: ", thrice)
    print(twice * thrice)
    return
def p2(given):

    print("Part 2 TBD")
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
