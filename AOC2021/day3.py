#!/usr/bin/env python3

input_file = 'inputs/day3'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def o2(given, index):
    if len(given) == 1:
        return given
    else:
        ones = []
        zeroes = []
        for x in given:
            if x[index] == '1':
                ones.append(x)
            elif x[index] == '0':
                zeroes.append(x)
        if len(ones) >= len(zeroes):
            return o2(ones,index+1)
        else:
            return o2(zeroes,index+1)
    
def co2(given, index):
    if len(given) == 1:
        return given
    else:
        ones = []
        zeroes = []
        for x in given:
            if x[index] == '1':
                ones.append(x)
            elif x[index] == '0':
                zeroes.append(x)
        if len(zeroes) <= len(ones):
            return co2(zeroes,index+1)
        else:
            return co2(ones,index+1)


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
    out1 = o2(given,0)[0]
    out2 = co2(given,0)[0]
    print("{}".format(int(out1,2)*int(out2,2)))
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
