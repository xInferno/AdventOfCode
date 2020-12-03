a = []
mi = ma = checksum = 0
with open('input.txt') as f:
    content = f.readlines()
    
for line in content:
    a.append(line.strip().split("\t"))

for sublist in a:
    for i in range(len(sublist)):
        sublist[i] = int(sublist[i])

# logic for part 1 goes below this line
#######################################

for sublist in a:
    mi = min(sublist)
    ma = max(sublist)
    checksum += ma - mi
    
print("Checksum:",checksum)
