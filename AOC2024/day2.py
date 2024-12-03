#!/usr/bin/env python3

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip().split() for x in infile]
    return infile

def compare(x):
        inc, dec, safe = False, False, True
        for i, y in enumerate(x):
            cur = int(x[i])
            if not i == len(x)-1:
                nxt = int(x[i+1])
            if i == 0: #first element
                if abs(cur-nxt) > 3: # unsafe - too large of a difference between numbers
                    return 0
                elif cur > nxt: # decrementing list
                    dec = True
                    continue
                elif cur < nxt: # incrementing list
                    inc = True
                    continue
                else: # elements are the same, therefore unsafe
                    safe = False
                    return 0
            elif i == len(x)-1: # final element
                if (dec and safe) or (inc and safe): # huzzah!
                    return 1
            else: # processing needed
                if abs(cur-nxt) > 3: # unsafe - too large of a difference between numbers
                    return 0
                elif cur > nxt: # decrementing
                    if dec:
                        continue
                    else: # no longer decrementing, unsafe
                        safe = False
                        return 0
                elif cur < nxt: # incrementing
                    if inc:
                        continue
                    else: # no longer incrementing, unsafe
                        safe = False
                        return 0
                else: # if we get here, the elements are equal - thus unsafe
                    safe = False
                    return 0
                
def p1(given):
    safe,index = 0,0
    for x in given:
        safe += compare(x)
    return str(safe)

def p2(given):
    safe = 0
    for x in given:
        ret = compare(x)
        safe += ret
        if ret:
            continue
        else: # test every case for removal of each item in turn
            for z in range(0,len(x)):
                copy = x.copy()
                del copy[z]
                ret = compare(copy)
                safe += ret
                if ret:
                    break
    return str(safe)

def main():
    given = process(input_file)       
    print("P1: " + p1(given))
    print("P2: " + p2(given))

if __name__ == '__main__':
    main()
