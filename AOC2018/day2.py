#!/usr/bin/env python3

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    answer = 0
    twice, thrice, found2, found3 = 0, 0, 0, 0
    for i in given:
        for j in i:
            if i.count(j) == 2:
                if found2:
                    continue
                else:
                    found2 = 1
                    twice += 1
            if i.count(j) == 3:
                if found3:
                    continue
                else:
                    found3 = 1
                    thrice += 1
        found2, found3 = 0, 0
    print(twice * thrice)
    return
def p2(given):
    outer = 0
    inner = outer + 1
    while outer < len(given):
        pos, err = 0, 0
        # process inner lines
        while inner < len(given):
            if err > 1: # too many errors
                err, pos = 0, 0
                break
            for i in range(0, len(given[outer])):
                if err > 1: # too many errors
                    err, pos = 0, 0
                    break
                if given[outer][i] != given[inner][i]:
                    err += 1
                    pos = i
                if i == len(given[outer])-1:
                    answer = ""
                    for j in range(0, len(given[outer])):
                        if j == pos: # skip the differing character
                            continue
                        else:
                            answer += given[outer][j]
                    print(answer)
                    # hack my way out
                    inner = 3000000
                    outer = 3000000
                    break

            inner += 1
        # end process inner lines
        outer += 1
        inner = outer + 1

    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
