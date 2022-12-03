#!/usr/bin/env python3

input_file = 'inputs/day1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    answer = 0
    for i in given:
        if i[0] == "+":
            answer += int(i[1:])
        elif i[0] == "-":
            answer -= int(i[1:])
        else:
            print("something is wrong")
    print(answer)
    return
def p2(given):
    seen = set()
    seen.add(0)
    answer = 0
    while True:
        for i in given:
            if i[0] == "+":
                answer += int(i[1:])
                if answer in seen:
                    print(answer)
                    return
                else:
                    seen.add(answer)
            elif i[0] == "-":
                answer -= int(i[1:])
                if answer in seen:
                    print(answer)
                    return
                else:
                    seen.add(answer)

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
