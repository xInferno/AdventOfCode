#!/usr/bin/env python3
input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip().split() for x in infile] 
    split = []
    for x in infile:
        split.append(x[0])
        split.append(x[1])
    list1 = split[::2]
    list2 = split[1::2]
    return list1, list2

def p1(l1,l2):
    l1s = sorted(l1)
    l2s = sorted(l2)
    ans = 0
    for x in range(0,len(l1s)):
        ans += (abs(int(l1s[x])-int(l2s[x])))
    print("P1 answer: " + str(ans))
    return

def p2(list1,list2):
    ans = 0
    for x in list1:
        ans += int(x) * list2.count(x)
    print("P2 answer: " + str(ans))
    return

def main():
    l1,l2 = process(input_file)       
    p1(l1,l2)
    p2(l1,l2)

if __name__ == '__main__':
    main()
