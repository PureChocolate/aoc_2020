import time
stime = time.time()
with open("chungus2.txt", "r") as f: bp = f.read().replace("B","1").replace("F","0").replace("R","1").replace("L","0").split("\n")
ma = 0
seats = []
for a in bp:
    num = int(a,2)
    seats.append(num)
    if num > ma: ma = num
print(ma)
print("---%s---:part1" % ((time.time() - stime)))

seats = sorted(seats)
for i in range(seats[0], seats[-1]+1):
    if i not in seats:
        print(i)
        break
    else: seats.pop(0)

print("---%s---" % ((time.time() - stime)))