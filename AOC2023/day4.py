#!/usr/bin/env python3
import re

input_file = 'inputs/day4'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    ans = 0
    winnums = []
    for x in given:
        cards = re.sub(r'^.*: ','',x).split("| ")
        winners = cards[0].split()
        data = cards[1].split()
        numwon = 0
        for i in winners:
            if i in data:
                if numwon == 0:
                    numwon = 1
                else:
                    numwon *= 2
        winnums.append(numwon)
    ans = sum(winnums)

    print("P1: " + str(ans))
        
    return

def p2(given):
    # Parts of this solution are taken from here: https://www.youtube.com/watch?v=NVLLDlOyrj4
    cardarray = [1] * len(given)
    for i,x in enumerate(given):
        cards = re.sub(r'^.*: ','',x).split("| ")
        winners = cards[0].split()
        data = cards[1].split()
        overlap = set(winners) & set(data) # idea from this came from the youtube link
        for j in range(len(overlap)): # for the next j card numbers, starting at zero
            cardarray[i+j+1] += cardarray[i] # this came from the youtube video... why +1? not sure.  
    
    print("P2: " + str(sum(cardarray)))
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
