#!/usr/bin/env python3

input_file = 'inputs/day3'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def solve(given, index, toggle):
    if len(given) == 1:
        return given
    else:
        ones = [x for x in given if x[index] == '1']
        zeroes = [x for x in given if x[index] == '0']
        if toggle == 1: # searching for o2
            if len(ones) >= len(zeroes):
                return solve(ones,index+1,1)
            else:
                return solve(zeroes,index+1,1)
        elif toggle == 0: # searching for co2
            if len(zeroes) <= len(ones):
                return solve(zeroes,index+1,0)
            else:
                return solve(ones,index+1,0)

def p1(given):
    ones = [0] * len(given[0])
    ostring, zstring = '', ''
    for x in given:
        for y in range(0, len(x)):
            if x[y] == '1':
                ones[y] += 1
    for x in ones:
        if x > len(given)/2:
            ostring += '1'
            zstring += '0'
        else:
            ostring += '0'
            zstring += '1'
    print("{}".format(int(ostring,2)*int(zstring,2)))
    return

def p2(given):
    out1 = solve(given,0,1)[0]
    out2 = solve(given,0,0)[0]
    print("{}".format(int(out1,2)*int(out2,2)))
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
