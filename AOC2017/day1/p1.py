captcha = 0

f = open("input.txt", "r").read().strip()

for i in range(len(f)):
    if (i + 1) != len(f):
        if f[i] == f[i + 1]:
            captcha += int(f[i])
    else:
        if f[i] == f[0]:
            captcha += int(f[i])

print(captcha)
