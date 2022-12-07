#!/usr/bin/env python3

# WARNING - this program requires the 'match' keyword, which
# requires python>3.10.

input_file = 'inputs/day2'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def compute(given, noun, verb):
    index = 0
    sanitized = given[0].split(",")
    sanitized = [int(x) for x in sanitized]

    # initialize memory
    sanitized[1] = noun
    sanitized[2] = verb

    while True:
        match int(sanitized[index]):
            case 99:
                break
            case 1:
                pos1 = sanitized[index+1]
                pos2 = sanitized[index+2]
                pos3 = sanitized[index+3]
                sanitized[pos3] = sanitized[pos1] + sanitized[pos2]
                index += 4
                continue
            case 2:
                pos1 = sanitized[index+1]
                pos2 = sanitized[index+2]
                pos3 = sanitized[index+3]
                sanitized[pos3] = sanitized[pos1] * sanitized[pos2]
                index += 4
                continue
            case _:
                print("Did not find matching opcode, bailing out")
                break
            
    return sanitized[0]

def p1(given):
    answer = compute(given, 12, 2)
    print("Number in position 0: ",answer)
    return
def p2(given):
    done = 0
    for i in range(0,100):
        if done:
            break
        else:
            for j in range(0,100):
                answer = compute(given,i,j)
                if answer == 19690720:
                    print("The answer to part 2 is:", 100 * i + j)
                    done = 1
                    break
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
