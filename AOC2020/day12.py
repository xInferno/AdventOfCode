#!/usr/bin/env python3
import re

input_file = 'inputs/day12'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    direction = 90
    xdelta = 0
    ydelta = 0
    for i in given:
        if i[0] == 'N':
            ydelta += int(re.search(r'\d+', i).group(0))
        elif i[0] == 'S':
            ydelta -= int(re.search(r'\d+', i).group(0))
        elif i[0] == 'E':
            xdelta += int(re.search(r'\d+', i).group(0))
        elif i[0] == 'W':
            xdelta -= int(re.search(r'\d+', i).group(0))
        elif i[0] == 'R':
            direction += int(re.search(r'\d+', i).group(0))
            if direction >= 360:
                direction -= 360
        elif i[0] == 'L':
            direction -= int(re.search(r'\d+', i).group(0))
            if direction < 0:
                direction += 360
        elif i[0] == 'F':
            if direction == 0:
                ydelta += int(re.search(r'\d+', i).group(0))
            elif direction == 180:
                ydelta -= int(re.search(r'\d+', i).group(0))
            elif direction == 90:
                xdelta += int(re.search(r'\d+', i).group(0))
            elif direction == 270:
                xdelta -= int(re.search(r'\d+', i).group(0))
            else:
                print("INVALID DIRECTION FOR FORWARD COMMAND")
                break
        else:
            print("INVALID COMMAND RECEIVED")

    print("Manhattan distance following old directions: {}".format(abs(xdelta)+abs(ydelta)))

            

    return
def p2(given):
    xdelta = 0
    ydelta = 0
    xway = 10
    yway = 1
    for i in given:
        if i[0] == 'N':
            yway += int(re.search(r'\d+', i).group(0))
        elif i[0] == 'S':
            yway -= int(re.search(r'\d+', i).group(0))
        elif i[0] == 'E':
            xway += int(re.search(r'\d+', i).group(0))
        elif i[0] == 'W':
            xway -= int(re.search(r'\d+', i).group(0))
        elif i[0] == 'L':
            direct = int(re.search(r'\d+', i).group(0))
            if direct == 270:
                temp = xway
                xway = yway
                yway = temp * -1
            elif direct == 180:
                yway = yway * -1
                xway = xway * -1
            elif direct == 90:
                temp = yway
                yway = xway
                xway = temp * -1
            else:
                print("INVALID ROTATION RECEIVED ON LEFT ROTATION")
        elif i[0] == 'R':
            direct = int(re.search(r'\d+', i).group(0))
            if direct == 90:
                temp = xway
                xway = yway
                yway = temp * -1
            elif direct == 180:
                yway = yway * -1
                xway = xway * -1
            elif direct == 270:
                temp = yway
                yway = xway
                xway = temp * -1
            else:
                print("INVALID ROTATION RECEIVED ON RIGHT ROTATION")
        elif i[0] == 'F':
            xdelta += xway * int(re.search(r'\d+', i).group(0))
            ydelta += yway * int(re.search(r'\d+', i).group(0))
        else:
            print("INVALID COMMAND RECEIVED")

    print("Manhattan distance following new instructions: {}".format(abs(xdelta)+abs(ydelta)))
    return
def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
