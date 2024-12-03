#!/usr/bin/env python3
import re

input_file = 'inputs/day3'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    sum = 0
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    for x in given:
        matches = pattern.findall(str(x))
        for y in matches:
            y = re.sub(r'mul\(','',y)
            y = re.sub(r'\)','',y)
            z, a = y.split(',')
            sum += int(z) * int(a)
    return str(sum)

def p2(given):
    sum = 0
    pattern = re.compile(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)')
    do = True
    for x in given:
        final = []
        matches = pattern.findall(str(x))
        for x in matches:
            if x == "do()":
                do = True
                continue
            elif x == "don't()":
                do = False
                continue
            else:
                if not do:
                    continue
                else:
                    final.append(x)
        for y in final:
            y = re.sub(r'mul\(','',y)
            y = re.sub(r'\)','',y)
            z, a = y.split(',')
            sum += int(z) * int(a)
    return str(sum)


def main():
    given = process(input_file)       
    print("P1: " + p1(given))
    print("P2: " + p2(given))

if __name__ == '__main__':
    main()
