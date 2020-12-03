captcha = 0

f = open("input.txt", "r").read().strip()

for i in range(len(f)):
    if (i + int(len(f)/2)) < len(f):
        if f[i] == f[i + int(len(f)/2)]:
            captcha += int(f[i])
    else:
        if f[i] == f[i - int(len(f)/2)]:
            captcha += int(f[i])

print(captcha)
