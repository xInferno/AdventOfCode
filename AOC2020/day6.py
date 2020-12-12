#!/usr/bin/env python3
import re

input_file = 'inputs/day6'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def f_or(given):
    found_letters = [0] * 26
    count = 0
    for i in given:
        for j in i:
            found_letters[ord(j)-97] = 1

    for i in found_letters:
        count += i

    return count

def f_and(given):
    yesall = [1] * 26
    count = 0
    for i in given:
        found = [0] * 26 
        for j in i:
            found[ord(j)-97] = 1
        for k in range(len(yesall)):
            if yesall[k] == 1 and found[k] == 0:
                yesall[k] = found[k]
    for i in yesall:
        count += i
    return count
def p1(given):
    count = 0
    proc = []
    for i in given:
        if i == '': # end of entry, count yesses
            count += f_or(proc)
            proc = []
        else:
             proc.append(i)
    return count


def p2(given):
    count = 0
    proc = []
    for i in given:
        if i == '': # end of entry, count yesses
            count += f_and(proc)
            proc = []
        else:
             proc.append(i)
    return count

def main():
    given = process(input_file)       
    print("The sum of the counts of people who answered 'yes' to any question is {}".format(p1(given)))
    print("The sum of the counts of people who answered 'yes' to all questions is {}".format(p2(given)))

if __name__ == '__main__':
    main()
