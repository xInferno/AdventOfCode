#!/usr/bin/env python3

nice_strings = 0

with open("input") as f:
    content = [x.strip() for x in f.readlines()]

for line in content:
    # priority to ignoring naughty strings
    x = 2
    double, gap = 0, 0
    while x < len(line):
        look = line[x-2] + line[x-1] + line[x]
        if look[0] == look[2]:
            gap = 1
        y = x + 1
        while y < len(line):
            look2 = line[y-1] + line[y]
            if look[0] == look2[0] and look[1] == look2[1]:
                double = 1
            y += 1
        x += 1
    if double == 1 and gap == 1:
        nice_strings += 1

print("There are",nice_strings,"nice strings")

