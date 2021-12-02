#!/usr/bin/env python3

input_file = 'inputs/day8'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given, sp):
    excode = 0
    acc = 0
    splist = []
    while sp != -1:
        # have we been here before?
        if sp in splist:
            excode = 1
            break
        try:
            ins, num = given[sp].split()
        except IndexError:
            break
        num = int(num)
        if ins == 'nop':
            splist.append(sp)
            sp += 1
            continue
        if ins == 'acc':
            acc += num
            splist.append(sp)
            sp += 1
            continue
        if ins == 'jmp':
            splist.append(sp)
            sp += num
            continue

    return excode, acc
def p2(given):
    count = 0
    for i in given:
        ins, num = i.split()
        if ins == 'nop':
            if int(num) == 0:
                count += 1
                continue # converting this to a jmp will cause an infinite loop
            else:
                test = given.copy()
                test[count] = "jmp " + num
                excode, acc = p1(test,0)
                if excode == 1:
                    count += 1
                    continue
                else:
                    return acc
        elif ins == 'jmp':
                test = given.copy()
                test[count] = "nop " + num
                excode, acc = p1(test,0)
                if excode == 1:
                    count += 1
                    continue
                else:
                    return acc
        else:
            count += 1
            continue
    return

def main():
    given = process(input_file)       
    _, acc = p1(given,0)
    print("Reached an instruction we've visited before, the accumulator value is: {}".format(acc))
    print("When the program exits successfully, the accumulator value is: {}".format(p2(given)))

if __name__ == '__main__':
    main()
