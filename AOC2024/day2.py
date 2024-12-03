#!/usr/bin/env python3

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip().split() for x in infile]
    return infile

def compare(x):
        print()
        inc, dec, safe = False, False, True
        for i, y in enumerate(x):
            cur = int(x[i])
            if not i == len(x)-1:
                nxt = int(x[i+1])
                print ("Current element: " + str(cur) + ", next element: " + str(nxt))
            if i == 0: #first element
                if abs(cur-nxt) > 3:
                    print("REPORT UNSAFE - too large of a difference between numbers. Difference is: " + str(abs(cur-nxt)))
                    return 0
                elif cur > nxt:
                    dec = True
                    print("Setting list to decrement")
                    continue
                elif cur < nxt:
                    inc = True
                    print("Setting list to increment")
                    continue
                else: # elements are the same, therefore unsafe by default
                    print("UNSAFE ON FIRST ELEMENT")
                    safe = False
                    return 0
            elif i == len(x)-1: # final element
                print("Reached final element")
                if (dec and safe) or (inc and safe):
                    print("This report is safe!")
                    return 1
            else: # processing needed
                if abs(cur-nxt) > 3:
                    print("REPORT UNSAFE - too large of a difference between numbers. Difference is: " + str(abs(cur-nxt)))
                    return 0
                elif cur > nxt: # decrementing
                    if dec:
                        continue
                    else:
                        print("REPORT UNSAFE - started as decrement, found increment")
                        safe = False
                        return 0
                elif cur < nxt:
                    if inc:
                        continue
                    else:
                        print("REPORT UNSAFE - started as increment, found decrement")
                        safe = False
                        return 0
                else:
                    print("REPORT UNSAFE - equal elements found")
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
        else:
            for z in range(0,len(x)):
                copy = x.copy()
                print("Testing removal of index: " + str(z))
                del copy[z]
                print("The copied array now looks like: " + str(copy))
                ret = compare(copy)
                safe += ret
                if ret:
                    break
    return str(safe)

def main():
    given = process(input_file)       
    #print("P1: " + p1(given))
    print("P2: " + p2(given))

if __name__ == '__main__':
    main()
