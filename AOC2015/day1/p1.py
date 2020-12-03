f = open("input.txt","r").read().strip()
floor = 0

for i in range(len(f)):
    if f[i] == "(":
        floor += 1
    elif f[i] == ")":
        floor -= 1
    else:
        print("error")

print("Santa is on",floor)


