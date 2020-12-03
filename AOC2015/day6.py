#!/usr/bin/env python3

lights = [ [0]*1000 for i in range(1000) ]
lights2 = [ [0]*1000 for i in range(1000) ]

def p1(commands):
    for command in commands:
        ins, fx, fy, lx, ly = process(command)
        if ins == 1:
            toggle(fx, fy, lx, ly)    
        elif ins == 2:
            on(fx, fy, lx, ly)
        elif ins == 3:
            off(fx, fy, lx, ly)
        else:
            print("invalid instruction")

    print("after all instructions, there are {} lights on".format(pri(1)))

def p2(commands):
    for command in commands:
        ins, fx, fy, lx, ly = process(command)
        if ins == 1 or ins == 2 or ins == 3:
            adj(ins, fx, fy, lx, ly)    
        else:
            print("invalid instruction")

    print("after all instructions, the total brightness is {}".format(pri(2)))
    
def pri(ins):
    count = 0
    x, y = 0, 0
    while x < 1000:
        while y < 1000:
            if ins == 1:
                if lights[x][y] == 1:
                    count += 1
            elif ins == 2:
                count += lights2[x][y]
            y += 1
        y = 0
        x += 1
    return count

def infile(infile):
    with open(infile) as f:
        content = [x.strip() for x in f.readlines()]
        return content

def process(line):
    ins, fx, fy, lx, ly = 0, 0, 0, 0, 0
    txt = [x for x in line.split()]

    if len(txt) == 4: # toggle command
        ins = 1
        fx, fy = txt[1].split(",")
        lx, ly = txt[3].split(",")
    elif txt[1] == 'on':
        ins = 2
        fx, fy = txt[2].split(",")
        lx, ly = txt[4].split(",")
    elif txt[1] == 'off':
        ins = 3
        fx, fy = txt[2].split(",")
        lx, ly = txt[4].split(",")
    else:
        print("invalid instruction")
        ins = -1

    return ins, fx, fy, lx, ly

def on(fx, fy, lx, ly):
    global lights
    x, y = int(fx), int(fy)
    while x <= int(lx):
        while y <= int(ly):
            lights[x][y] = 1
            y += 1
        y = int(fy)
        x += 1

def off(fx, fy, lx, ly):
    global lights
    x, y = int(fx), int(fy)
    while x <= int(lx):
        while y <= int(ly):
            lights[x][y] = 0
            y += 1
        y = int(fy)
        x += 1

def toggle(fx, fy, lx, ly):
    global lights
    x, y = int(fx), int(fy)
    while x <= int(lx):
        while y <= int(ly):
            if lights[x][y] == 1:
                lights[x][y] = 0
            elif lights[x][y] == 0:
                lights[x][y] = 1
            else:
                print("invalid toggle")
            y += 1
        y = int(fy)
        x += 1

def adj(ins, fx, fy, lx, ly):
    global lights2
    x, y = int(fx), int(fy)
    while x <= int(lx):
        while y <= int(ly):
            if ins == 1:
                lights2[x][y] += 2
            elif ins == 2:
                lights2[x][y] += 1
            elif ins == 3:
                if lights2[x][y] == 0:
                    lights2[x][y] = 0
                else:
                    lights2[x][y] -= 1
            else:
                print("invalid toggle")
            y += 1
        y = int(fy)
        x += 1

def main():
    commands = infile('inputs/day6')
    p1(commands)
    p2(commands)

if __name__ == "__main__":
    main()
