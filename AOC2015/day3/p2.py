f = open("input.txt","r").read().strip()

sx = sy = rx = ry = 0

santa = ["0,0"]
robo = ["0,0"]
uniq = []
santaturn = 1

for i in range(len(f)):
    if santaturn == 1:
        if f[i] == ">":
            sx += 1
        elif f[i] == "<":
            sx -= 1
        elif f[i] == "^":
            sy += 1
        elif f[i] == "v":
            sy -= 1
        else:
            print("Invalid character")
    elif santaturn == 0:
        if f[i] == ">":
            rx += 1
        elif f[i] == "<":
            rx -= 1
        elif f[i] == "^":
            ry += 1
        elif f[i] == "v":
            ry -= 1
        else:
            print("Invalid character")
    else:
        print("santaturn invalid value")
    if santaturn == 1:
        toadd = str(sx)
        toadd += ","
        toadd += str(sy)
        santa.append(toadd)
        santaturn = 0
    elif santaturn == 0:
        toadd = str(rx)
        toadd += ","
        toadd += str(ry)
        robo.append(toadd)
        santaturn = 1
    else:
        print("santaturn invalid value")

for x in santa:
    if x not in uniq:
        uniq.append(x)
for y in robo:
    if y not in uniq:
        uniq.append(y)

print("Number of houses visited:",len(uniq))

