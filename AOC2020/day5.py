#!/usr/bin/env python3
import re

input_file = 'inputs/day5'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def getrow(given):
    top = 127
    bot = 0
    count = 1    
    for i in range(6):
        if given[i] == 'F':
            top = top - (64 / count)
        elif given[i] == 'B':
            bot = bot + (64 / count)
        else:
            print("Error: invalid entry at position {}".format(i))
            break
        count *= 2

    if given[6] == 'F':
        return bot
    elif given[6] == 'B':
        return top
    else:
        print("Error - sixth position not valid or see previous error")
        return None

# This may come back to bite me, but it's easier right now to hardcode the steps instead of relying on a for loop
def getcol(given):
    top = 7
    bot = 0
    
    if given[7] == 'L':
        top = top - 4
    elif given[7] == 'R':
        bot = bot + 4
    else:
        print("Error in first position")
        return None

    if given[8] == 'L':
        top = top - 2
    elif given[8] == 'R':
        bot = bot + 2
    else:
        print("Error in second position")
        return None

    if given[9] == 'L':
        return bot 
    elif given[9] == 'R':
        return top 
    else:
        print("Error in third position")
        return None



def p1(given):
    high = 0
    for i in given:
        row = getrow(i)
        col = getcol(i)
        sid = row * 8 + col
        if sid > high:
            high = sid

    print("The highest seat ID is: {}".format(high))
    return
def p2(given):
    sids = []
    count = 0
    for i in given:
        row = getrow(i)
        col = getcol(i)
        sid = row * 8 + col
        sids.append(sid)
    ssids = sorted(sids)
    for i in ssids:
        if count == 0:
            count += 1
            continue
        test = ssids[count]+1
        if test+1 == ssids[count+1]:
            print("Your seat ID is: {}".format(test))
            return
        count += 1
def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
