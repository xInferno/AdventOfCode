#!/usr/bin/env python3

input_file = 'inputs/day3'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0
    for i in given:
        first, second = i[:int(len(i)/2)], i[int(len(i)/2):]
        for j in first:
            if j in second:
                answer += int(priorities.find(j) + 1)
                break
        
    print(answer)
    return
def p2(given):
    priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0
    first, second, third = "", "", ""
    for i in given:
        if (given.index(i) + 1 ) % 3 == 0: # third entry, find
            third = i
            for j in first:
                if j in second and j in third:
                    answer += int(priorities.find(j) + 1)
                    first, second, third = "", "", ""
                    break
        elif (given.index(i) + 1 ) % 3 == 1: # first entry
            first = i
            continue
        elif (given.index(i) + 1 ) % 3 == 2: # second entry
            second = i
            continue
    print(answer)
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
