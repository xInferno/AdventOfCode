#!/usr/bin/env python3

nice_strings = 0
vowels = "aeiou"
naughty_strings = ["ab","cd","pq","xy"]


with open("input") as f:
    content = [x.strip() for x in f.readlines()]

for line in content:
    # priority to ignoring naughty strings
    x = 1
    double, bnaughty = 0, 0
    while x < len(line):
        look = line[x-1] + line[x]
        if look in naughty_strings:
            bnaughty = -1
            break
        if line[x] == line[x-1]:
            double = 1
        x += 1
    if bnaughty == -1 or double == 0: # prohibited string or no doubles, move to the next line
        continue
    # check for vowels
    vowel_count = 0
    for ch in line:
        if ch in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        nice_strings += 1

print("There are",nice_strings,"nice strings")

