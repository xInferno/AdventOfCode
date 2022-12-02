#!/usr/bin/env python3

input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    mx, gmx = 0, 0
    for i in given:
      if i.strip() == '':
        if mx > gmx:
           gmx = mx
        mx = 0
      else:
        mx += int(i)
    print(gmx)
    return
def p2(given):
    mx, gmx1, gmx2, gmx3 = 0, 0, 0, 0
    for i in given:
      if i.strip() == '':
        if mx > gmx1:
           gmx3 = gmx2
           gmx2 = gmx1
           gmx1 = mx
        elif mx > gmx2:
           gmx3 = gmx2
           gmx2 = mx
        elif mx > gmx3:
           gmx3 = mx
        mx = 0
      else:
        mx += int(i)
    print(gmx3, "+", gmx2, "+", gmx1, "=", gmx3+gmx2+gmx1)
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
