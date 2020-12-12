#!/usr/bin/env python3

input_file = 'inputs/day3'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def mapgen(given):
    # find the size of the array
    sizey = len(given)
    sizex = sizey * 10 
    mapa = [[0]*sizex for i in range(sizey)]
    # populate the map
    rownum, colnum, offset = 0, 0, 0
    for row in given: #for every y value
        while colnum < sizex:
            #duplicate characters until we get to index 31, then return to index 0
            if colnum % len(given[0]) == 0:
                offset = 0
            mapa[rownum][colnum] = row[offset]
            colnum += 1
            offset += 1
        colnum, offset = 0, 0
        rownum += 1
    return mapa

def slope(mapa, rowdelta, coldelta):
    trees = 0
    dcol = coldelta
    rownum, colnum = 0, 0
    while rownum < len(mapa):
        if mapa[rownum][colnum] == '#':
            trees += 1
        colnum += coldelta
        rownum += rowdelta
    return trees

def p1(given):
    mapa = mapgen(given)
    print(slope(mapa, 1, 3))

def p2(given):
    mapa = mapgen(given)
    a1 = slope(mapa, 1, 1)
    a2 = slope(mapa, 1, 3)
    a3 = slope(mapa, 1, 5)
    a4 = slope(mapa, 1, 7)
    a5 = slope(mapa, 2, 1)
    print("{} {} {} {} {}".format(a1,a2,a3,a4,a5))
    print(a1*a2*a3*a4*a5)

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
