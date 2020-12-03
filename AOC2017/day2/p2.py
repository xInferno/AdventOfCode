a = []
checksum = 0
with open('input.txt') as f:
    content = f.readlines()
    
for line in content:
    a.append(line.strip().split("\t"))

for sublist in a:
    for i in range(len(sublist)):
        sublist[i] = int(sublist[i])

# Logic for part 2 goes below this line
#########################################

# this is so ugly D:
for sublist in a:
    for x in range(len(sublist)):
        for y in range(x+1, len(sublist)):
            if sublist[x] % sublist[y] == 0: checksum += (sublist[x] / sublist[y])
            elif sublist[y] % sublist[x] == 0: checksum += (sublist[y] / sublist[x])
    
    
    
print("Checksum:",checksum)
