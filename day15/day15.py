from collections import defaultdict
with open("test.txt","r") as f: sNUms = f.read().split(",")
seen = defaultdict(lambda: [0,0,0])
spoken = []
for a in range(len(sNUms)):
    seen[sNUms[a]] = [0,a+1,a+1]
    spoken.append(sNUms[a])

i = 3
while(i < 10):
    rSpo = list(reversed(spoken))
    print(spoken, "Waaa")
    i += 1
    if seen[rSpo[0]][0] == 0:
        print(rSpo,"rrrrrr")
        spoken.append(0)
        seen[rSpo[0]][0] = 1 
        seen[rSpo[1]][1] = i
    else:
        print(seen[rSpo[0]])
        print(seen[rSpo[0]][1],seen[rSpo[0]][2])
        new = seen[rSpo[0]][1] - seen[rSpo[0]][2]
        if new in spoken:
            index = spoken.index(new)
            spoken.append(new)
            seen[new] = [1, i,index]
            continue
        spoken.append(new)
        seen[new] = [0,i,i]
print(spoken[:11])


# lNum = sNUms[-1]
# turn = 4
# while(lNum < 2020):
#     if seen[lNum][0] == 0: 
#         lNum = 0:
#         seen[lNum][0] = 1
#         seen[lNum][1] = turn
#         seen[lNum][2] = 0
#     else:
#         lNum = seens[lNum][1] - seen[lNum][2]

#     turn += 1


# print(seen)