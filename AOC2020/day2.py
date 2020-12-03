#!/usr/bin/env python3

input_file = 'inputs/day2'
input_test = '5-8 f: fxffmfff'
valid = 0

def process(given):
    with open(given) as f:
        inlist = f.read().splitlines()
    return inlist

def sub(given):
    policy, password = given.split(":")
    number, letter = policy.split()
    minimum, maximum = number.split("-")
    return minimum, maximum, letter, password.strip()

def p1():
    global valid
    inlist = process(input_file)
    for x in inlist:
        count = 0
        minimum, maximum, letter, password = sub(x)
        for i in password:
            if i == letter:
                count += 1
        if count >= int(minimum):
            if count <= int(maximum):
                valid += 1
    print(valid)
    valid = 0
    return

def p2():
    global valid
    inlist = process(input_file)
    for x in inlist:
        b1, b2 = 0, 0
        p1, p2, letter, password = sub(x)
        if password[int(p1)-1] == letter:
            b1 = 1
        if password[int(p2)-1] == letter:
            b2 = 1
        if b1 ^ b2:
            valid += 1
    print(valid)
    return

def main():
    p1()
    p2()

if __name__ == '__main__':
    main()
