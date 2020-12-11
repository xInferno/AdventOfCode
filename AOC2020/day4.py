#!/usr/bin/env python3
import re

input_file = 'inputs/day4'

def process(given):
    with open(given) as f:
        infile = f.readlines()
    infile = [x.strip() for x in infile]
    return infile

def p1(given):
    # capture the flag... or something
    byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf, cidf = 0, 0, 0, 0, 0, 0, 0, 0
    valid = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:", "cid:"] 
    count = 0 
    # read each line into a string
    # set flags based on presence of strings
    # when double newline is reached process flags and increment 'valid' if valid
    for i in given:
        if i == '': #end of entry
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
    print("Number of valid passports for part 1: {}".format(count))
    return

def p2(given):
    byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf = 0, 0, 0, 0, 0, 0, 0
    count = 0 
    for i in given:
        if i == '': #end of entry
            if byrf and iyrf and eyrf and hgtf and hclf and eclf and pidf:
                count += 1
            byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf, cidf = 0, 0, 0, 0, 0, 0, 0, 0
        else:
            if re.search("byr:([1][9][2-9][0-9]|[[2][0][0][0-2])",i) is not None:
                byrf = 1
            if re.search("iyr:(201[0-9]|2020)",i) is not None: 
                iyrf = 1
            if re.search("eyr:(202[0-9]|2030)",i) is not None:
                eyrf = 1
            if re.search("hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)",i) is not None:
                hgtf = 1
            if re.search("hcl:#([0-9]|[a-f]){6}\\b",i) is not None:
                hclf = 1
            if re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)",i) is not None:
                eclf = 1
            if re.search("pid:[0-9]{9}\\b",i) is not None:
                pidf = 1
    print("Number of valid passports for part 2: {}".format(count))
    return

# Wrote this while debugging part 2 to make sure I was using the regex library correctly...
def pone(given):
    byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf, cidf = 0, 0, 0, 0, 0, 0, 0, 0
    count = 0 
    for i in given:
        if i == '': #end of entry
            if byrf and iyrf and eyrf and hgtf and hclf and eclf and pidf:
                count += 1
            byrf, iyrf, eyrf, hgtf, hclf, eclf, pidf, cidf = 0, 0, 0, 0, 0, 0, 0, 0
        else:
            if re.search("byr:",i) is not None:
                byrf = 1
            if re.search("iyr:",i) is not None: 
                iyrf = 1
            if re.search("eyr:",i) is not None:
                eyrf = 1
            if re.search("hgt:",i) is not None:
                hgtf = 1
            if re.search("hcl:",i) is not None:
                hclf = 1
            if re.search("ecl:",i) is not None:
                eclf = 1
            if re.search("pid:",i) is not None:
                pidf = 1
    print("Number of valid passports for part 1 (using regex): {}".format(count))
    return


def main():
    given = process(input_file)       
    #p1(given)
    pone(given)
    p2(given)

if __name__ == '__main__':
    main()
