#!/usr/bin/env python3

input_file = 'inputs/day5'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.replace("\n","") for x in infile]
    return infile

def gen(given):

    height, num = 0, 0
    # figure out how high the container towers are
    for i in given:
        if i == "":
            height -= 1
            break
        else:
            height += 1
    # figure out how many containers there are
    # conveniently right above the empty string
    x = given[height]
    num = int((x[len(x)-2]))

    # create the 2d array
    master = []
    for i in range(0,num):
        master.append([])

    count = height-1 # number of times to loop through
    while count >= 0: # build from the bottom-up
        index = 0 # horizontal 
        while (index*4+1) < len(given[count]):
            item = given[count][index*4+1]
            if item != " ":
                master[index].append(item)
            index += 1
        count -= 1
    return master
    
def p1(given, master):
    process = 0
    for i in given:
        if process == 1:
            inst = i.split(" ")
            qnty, src, dst = int(inst[1]), int(inst[3])-1, int(inst[5])-1
            for j in range(0,qnty):
                master[dst].append(master[src].pop())
        # this just gets us to the processing point
        elif i == "":
            process = 1
        else:
            continue

    answer = ""
    for i in range(0,len(master)):
        answer = answer + master[i][len(master[i])-1]
    print(answer)
    return

def p2(given, master):
    process = 0
    temp = []
    for i in given:
        if process == 1:
            inst = i.split(" ")
            qnty, src, dst = int(inst[1]), int(inst[3])-1, int(inst[5])-1
            for j in range(0,qnty):
                temp.append(master[src].pop())
            for j in range(0,qnty):
                master[dst].append(temp.pop())
        elif i == "":
            process = 1
        else:
            continue

    answer = ""
    for i in range(0,len(master)):
        answer = answer + master[i][len(master[i])-1]
    print(answer)
    return

def main():
    given = process(input_file)       
    master1 = gen(given) 
    master2 = gen(given) # separate copies for each part
    p1(given, master1)
    p2(given, master2)

if __name__ == '__main__':
    main()
