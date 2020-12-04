#!/usr/bin/env python3

input_file = 'inputs/day4'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    # capture the flag... or something
    byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf, cidf = 0, 0, 0, 0, 0, 0, 0, 0
    valid = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid", "cid:"] 
    count = 0 
    # read each line into a string
    # set flags based on presence of strings
    # when double newline is reached process flags and increment 'valid' if valid
    for i in given:
        if i == '\n': #end of entry
            print("end of entry")
            if byrf and iyrf and eyrf and hgtf and hclf and eclf and pidf:
                count += 1
            byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf, cidf = 0, 0, 0, 0, 0, 0, 0, 0
        else:
            if valid[0] in i:
                byrf = 1
            if valid[1] in i:
                iyrf = 1
            if valid[2] in i:
                eyrf = 1
            if valid[3] in i:
                hgtf = 1
            if valid[4] in i:
                hclf = 1
            if valid[5] in i:
                eclf = 1
            if valid[6] in i:
                pidf = 1
            if valid[7] in i:
                cidf = 1
    print("Number of valid passports: {}".format(count))
    return

def p2(given):
    print("part 2 TBD")
    return

def main():
    given = process(input_file)       
    p1(given)
    p2(given)

if __name__ == '__main__':
    main()
