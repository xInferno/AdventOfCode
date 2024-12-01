#!/usr/bin/env python3
import re 

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    # thresholds
    red = 12
    green = 13
    blue = 14
    ans = 0

    for i,x in enumerate(given):
        trim = re.sub(r'^.*: ', '', x)
        pulls = trim.split("; ")
        valid = True
        for y in pulls:
            colors = y.split(", ")
            for z in colors:
                if 'red' in z:
                    rnum = re.findall(r'\d+', z)
                    if int(rnum[0]) > red:
                        valid = False
                if 'blue' in z:
                    bnum = re.findall(r'\d+', z)
                    if int(bnum[0]) > blue:
                        valid = False
                if 'green' in z:
                    gnum = re.findall(r'\d+', z)
                    if int(gnum[0]) > green:
                        valid = False
        if valid:
            ans += i+1
    print("P1: " + str(ans))
    return

def p2(given):
    ans = 0 
    for x in given:
        red = 0
        blue = 0
        green = 0
        trim = re.sub(r'^.*: ', '', x)
        pulls = trim.split("; ")
        for y in pulls:
            colors = y.split(", ")
            for z in colors:
                if 'red' in z:
                    rnum = re.findall(r'\d+', z)
                    if int(rnum[0]) > red:
                        red = int(rnum[0])
                if 'blue' in z:
                    bnum = re.findall(r'\d+', z)
                    if int(bnum[0]) > blue:
                        blue = int(bnum[0])
                if 'green' in z:
                    gnum = re.findall(r'\d+', z)
                    if int(gnum[0]) > green:
                        green = int(gnum[0])
            # end of pulls
        ans += (red * green * blue)
        # end of game
    print("P2: " + str(ans))


    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
