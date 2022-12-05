#!/usr/bin/env python3

input_file = 'inputs/day4'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def solve(given): # makes more sense to solve today in a single function
    answer1, answer2 = 0, 0
    for i in given:
        t1 = i.split(",")
        t2 = t1[0].split("-")
        t3 = t1[1].split("-")
        first = set()
        second = set()
        for j in range(int(t2[0]),int(t2[1])+1):
            first.add(j)
        for j in range(int(t3[0]),int(t3[1])+1):
            second.add(j)
        if first.issubset(second) or second.issubset(first):
            answer1 += 1
        for j in first:
            if j in second:
                answer2 += 1
                break
    print(answer1)
    print(answer2)
    return

def main():
    given = process(input_file)       
    solve(given)

if __name__ == '__main__':
    main()
