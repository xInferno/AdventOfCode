#!/usr/bin/env python3

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    # playing with tuples today
    opponent = ("A", "B", "C")
    me = ("X", "Y", "Z")
    points = 0
    for i in given:
        if i[2] == me[0]: #rock
            points += 1
            if i[0] == opponent[2]: #win
                points += 6
            elif i[0] == opponent[0]: #draw
                points += 3
        elif i[2] == me[1]: #paper
            points += 2
            if i[0] == opponent[0]: #win
                points += 6
            elif i[0] == opponent[1]: #draw
                points += 3
        elif i[2] == me[2]: #scissors
            points += 3
            if i[0] == opponent[1]: #win
                points += 6
            elif i[0] == opponent[2]: #draw
                points += 3
    print(points)
    return

def p2(given):
    opponent = ("A", "B", "C")
    result = ("X", "Y", "Z") 
    points = 0
    for i in given:
        if i[2] == result[0]: #lose
            if i[0] == opponent[0]: #rock, throw scissors
                points += 3
            elif i[0] == opponent[1]: #paper, throw rock
                points += 1
            elif i[0] == opponent[2]: #scissors, throw paper
                points += 2
        elif i[2] == result[1]: #draw
            if i[0] == opponent[0]: #rock
                points += 4
            elif i[0] == opponent[1]: #paper
                points += 5
            elif i[0] == opponent[2]: #scissors
                points += 6
        elif i[2] == result[2]: #win
            if i[0] == opponent[0]: #rock, throw paper
                points += 8
            elif i[0] == opponent[1]: #paper, throw scissors
                points += 9
            elif i[0] == opponent[2]: #scissors, throw rock
                points += 7
    print(points)
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
