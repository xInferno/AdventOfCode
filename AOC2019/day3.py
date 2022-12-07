#!/usr/bin/env python3

input_file = 'inputs/day3_sample1'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    w1_path = given[0].split(",")
    w2_path = given[1].split(",")
    w1_all_coords = set((0,0))
    w2_all_coords = set((0,0))
    w1_pos = [0,0]
    w2_pos = [0,0]


    ############
    # wire 1 path generation
    ############
    for i in w1_path:
        instruction = i[0]
        distance = int(i[1:])
        match instruction:
            case 'R':
                for j in range(0,distance):
                    w1_pos[0] += 1
                    w1_all_coords.add((w1_pos[0],w1_pos[1]))
            case 'L':
                for j in range(0,distance):
                    w1_pos[0] -= 1
                    w1_all_coords.add((w1_pos[0],w1_pos[1]))
            case 'U':
                for j in range(0,distance):
                    w1_pos[1] += 1
                    w1_all_coords.add((w1_pos[0],w1_pos[1]))
            case 'D':
                for j in range(0,distance):
                    w1_pos[1] -= 1
                    w1_all_coords.add((w1_pos[0],w1_pos[1]))
            case _:
                print("No instruction found")
                break

    ############
    # wire 2 path generation
    ############
    for i in w2_path:
        instruction = i[0]
        distance = int(i[1:])
        match instruction:
            case 'R':
                for j in range(0,distance):
                    w2_pos[0] += 1
                    w2_all_coords.add((w2_pos[0],w2_pos[1]))
            case 'L':
                for j in range(0,distance):
                    w2_pos[0] -= 1
                    w2_all_coords.add((w2_pos[0],w2_pos[1]))
            case 'U':
                for j in range(0,distance):
                    w2_pos[1] += 1
                    w2_all_coords.add((w2_pos[0],w2_pos[1]))
            case 'D':
                for j in range(0,distance):
                    w2_pos[1] -= 1
                    w2_all_coords.add((w2_pos[0],w2_pos[1]))
            case _:
                print("No instruction found")
                break

    
    both_set = w1_all_coords.intersection(w2_all_coords)
    both = list(both_set)

    # figure out manhattan distances
    distances = []
    for i in both:
        if i == 0: ## ignore origin
            continue
        else:
            distances.append(abs(int(i[0]))+abs(int(i[1])))
    print("Minimum distance:", min(distances))
    return

def p2(given):
    # oh god make the pain stop
    w1_path = given[0].split(",")
    w2_path = given[1].split(",")
    w1_all_coords = []
    w2_all_coords = []
    w1_pos = [0,0]
    w2_pos = [0,0]

    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
