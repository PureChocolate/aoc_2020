import time
stime = time.time()
with open("chungus2.txt", "r") as f: seats = f.read().strip().replace("B","1").replace("F","0").replace("R","1").replace("L","0").split("\n")

print("---%s---:parsed" % ((time.time() - stime)))
ma = 0
for i in range(len(seats)):
    seats[i] = int(seats[i],2)
    if ma < seats[i]: ma = seats[i]

print(ma)
print("---%s---:part1" % ((time.time() - stime)))
print(max(set(range(seats[len(seats)-1])[1:]) -set(seats)))
del(seats)
print("---%s---" % ((time.time() - stime)))
