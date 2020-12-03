f = open("input.txt","r").read().strip()
floor = 0
for i in range(len(f)):
    if f[i] == "(":
        floor += 1
    elif f[i] == ")":
        floor -= 1
        if floor == -1:
            print("Position",i + 1,"causes Santa to enter the basement for the first time")
    else:
        print("error")

print("Santa is on",floor)


