#!/usr/bin/env python3
import re
input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    ans = 0
    for x in given:
      m = re.findall(r"\d", x)
      n = m[0] + m[-1]
      ans += int(n)
    print("P1 ans: " + str(ans))
    return
def p2(given):
    # jeeeeez part 2 is way harder than part 1 this year
    ans = 0
    numarr = ["one","two","three","four","five","six","seven","eight","nine"] 
    for x in given:
        d1, d2 = 0, 0
        for i in range(0,len(x)): # i is the index
            test = x[:i+1] # off-by-one error - x[0:0] returns nothing and throws off processing
            if x[i].isdigit():
                d1 = x[i]
                break
            for index,item in enumerate(numarr,1):
                if item in test:
                  d1 = index
                  break
            if d1 != 0:
                break
        for i in range(0, len(x)):
            index = len(x) - i 
            test = x[-i-1:] # I don't quite understand why this works???
            if x[index-1].isdigit():
                d2 = x[index-1]
                break
            for index,item in enumerate(numarr,1):
                if item in test:
                  d2 = index
                  break
            if d2 != 0:
              break

        ans += int(str(d1) + str(d2))

    print("P2 ans: " + str(ans))
    return


def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
