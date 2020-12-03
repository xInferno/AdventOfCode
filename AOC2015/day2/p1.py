t = l = w = h = 0

with open("input.txt") as f:
    content = f.readlines()

for line in content:
   l,w,h = line.split("x")
   t += (2 * int(l) * int(w)) + (2 * int(w) * int(h)) + (2 * int(h) * int(l)) + min(int(l) * int(w), int(w) * int(h), int(h) * int(l))

print("You need",t,"feet of paper")

