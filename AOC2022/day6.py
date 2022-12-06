#!/usr/bin/env python3

input_file = 'inputs/day6'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def solve(given,part):
    # yay! a sliding window!
    window = []
    position, size  = 0, 0
    if part == 1:    # makes more sense
        size = 3     # to do it this way
    elif part == 2:  # than it does to have
        size = 13    # two separate functions
    else:
        print("invalid part number")
        return
    for i in given[0]:
        if len(window) < size:
            window.append(i)
            position += 1
            continue
        else:
            window.append(i)
            position += 1
            if len(set(window)) == len(window): # all items are unique
                print("Position:", position)
                break
            else:
                window.pop(0)
                continue
    return

def main():
    given = process(input_file)       
    solve(given,1)
    solve(given,2)

if __name__ == '__main__':
    main()
