from collections import defaultdict
with open("in10.txt","r") as f : data = f.read().strip().split("\n")
data = list(map(int,data))
data.append(max(data) + 3)
diff = {3:0,2:0,1:0,"ways": 0}
data = sorted(data)

def run(dataV):
    prev = 0
    for a in dataV:
        if a == 0: continue
        # print(a,prev)
        if 1 <= a - prev <= 3:
            diff[a-prev] += 1
            prev = a
            if a == max(dataV):
                return True
        else: return False

def poppables(data):
    popable = []
    d = 1
    while (d < len(data)-2):
        dL = data[d] - data[d-1]
        dR = data[d+1] - data[d]
        if dL + dR <=3:
            popable.append(data[d])
        d += 1
    return popable

def popper(popable):
    datP = data.copy()
    pops = popable
    for x in pops:
        datP.remove()

### Stupid approach ish, may try to finish up later 
# print(poppables())
# poping = 0
# for x in range(len(poppables())):
#     temp = data.copy()
#     pops = poppables()
#     while(len(pops) >= 0):
#         # print(pops)
#         # print(diff["ways"], "ways")
#         # print(poping, pops,len(pops),len(pops[:poping]))
#         if pops == []: break
#         try:
#             temp.remove(pops.pop(poping))
#             if run(temp) : diff["ways"] += 1
#         except IndexError:
#             if len(pops) >= 2:
#                 a = 0
#                 while(a < len(pops)):
#                     if pops == []: break
#                     temp.remove(pops.pop(a))
#                     a += 1
#                 if run(temp) : diff["ways"] += 1
#             else: break           
#     poping += 1

#p2
dp = defaultdict(int)
dp[0] = 1
for x in data:
    dp[x] += dp[x-1] + dp[x-2] + dp[x-3]

run(data)
print(diff[3] * diff[1],dp[max(data)])
