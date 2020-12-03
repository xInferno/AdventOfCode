#!/usr/bin/env python3

def p1():
    print("---Part 1---")
    f = open("../inputs/day1","r")

    a, b = [], []
    ans1, ans2, flag = 0, 0, 0
    for i in f.readlines():
        if i.strip():
            if flag:
                b.append(int(i))
            a.append(int(i))
            flag = 1

    for i in a:
        for j in b:
            if j + i == 2020:
                ans1 = i
                ans2 = j
                break

    print(ans1)
    print(ans2)
    print(ans1*ans2)

def p2():
    print("---Part 2---")
    f = open("../inputs/day1","r")
    a, b, c = [], [], []
    ans1, ans2, ans3, f1, f2 = 0, 0, 0, 0, 0
    for i in f.readlines():
        if i.strip():
            if f1:
                if f2:
                    c.append(int(i))
                b.append(int(i))
            a.append(int(i))
            if f1:
                f2 = 1
            f1 = 1

    for i in a:
        for j in b:
            for k in c:
                if k + j + i == 2020:
                    ans1 = i
                    ans2 = j
                    ans3 = k 
                    break

    print(ans1)
    print(ans2)
    print(ans3)
    print(ans1*ans2*ans3)

def main():
    p1()
    p2()

if __name__ == '__main__':
    main()
