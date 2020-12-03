t = l = w = h = 0

with open("input.txt") as f:
    content = f.readlines()

for line in content:
   l,w,h = line.split("x")
   t += (2*int(l) + 2*int(w) + 2*int(h) + (int(l)*int(w)*int(h)) - 2*(max(int(l),int(w),int(h))))

print("You need",t,"feet of ribbon")

