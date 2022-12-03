#!/usr/bin/env python3

input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [int(x.strip()) for x in infile]
    return infile

def calculate_fuel(given, prev):
    if given <= 0:
        return prev
    else:
        return calculate_fuel(int(given/3)-2,given)+prev

def p1(given):
    answer = 0
    for i in given:
        answer += (int(i/3)-2)
    print(answer)
    return
def p2(given):
    answer, moarfuel = 0, 0
    ## recursion? on DAY ONE?!
    for i in given:
        moarfuel += calculate_fuel(int(i/3)-2, 0)      
        answer += moarfuel
        moarfuel = 0
    print(answer)
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
