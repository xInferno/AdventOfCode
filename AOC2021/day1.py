#!/usr/bin/env python3

input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [int(x.strip()) for x in infile]
    return infile

def p1(given): 
    ans = 0
    for i in range(1, len(given)):
        if given[i] > given[i-1]:
            ans+=1
    print(ans)
    return
def p2(given):
    s1, s2, ans = 0, 0, 0
    for i in range(3, len(given)):
        s1 = given[i-3] + given[i-2] + given[i-1]
        s2 = given[i-2] + given[i-1] + given[i]
        if s1 < s2:
            ans+=1
    print(ans)
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)
if __name__ == '__main__':
    main()
