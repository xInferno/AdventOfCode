f = open("input.txt","r").read().strip()

x = y = 0

visited = ["0,0"]
uniq = []

for i in range(len(f)):
    if f[i] == ">":
        x += 1
    elif f[i] == "<":
        x -= 1
    elif f[i] == "^":
        y += 1
    elif f[i] == "v":
        y -= 1
    else:
        print("Invalid character")
    toadd = str(x)
    toadd += ","
    toadd += str(y)
    visited.append(toadd)

for x in visited:
    if x not in uniq:
        uniq.append(x)

print("Number of houses visited:",len(uniq))

