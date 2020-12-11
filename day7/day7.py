import time
with open("ihBa.txt", "r") as f: 
    stime = time.perf_counter()
    ttime = time.perf_counter()
    lr = f.read().strip().replace(" bags contain ","-").replace(" bag, ","-").replace(" bags, ", "-").replace(" bag.", "-").replace(" bags.", "-").split("\n")
rules = {}
p2 = {}
nums = {}
bags = set()
nbags = set()
for t in lr:
    s = ""
    t = t.split("-")[:-1]
    if "no other" in t: 
        rules[t[0]] = 0
        nbags.add(t[0])
        continue
    else:
        tr = []
        for r in t[1:]: 
            s += r[2:] + "&"
            tr.append(int(r[0]))
        nums[t[0]] = tr
        rules[t[0]] = s[:-1]
    if "shiny gold" in rules[t[0]]: 
        bags.add(t[0])

print("----%s-----:parsed" % (stime - time.perf_counter()))
stime = time.perf_counter()

def canHold2(bag):
    if bag in bags:
        return True
    elif rules[bag] == 0:
        return False
    else:
        for i in rules[bag].split("&"):
            if i in nbags: continue
            if canHold2(i): 
                bags.add(bag)
                return True
            else: nbags.add(i)

def part1():    
    line = 0
    c = 0
    for b in rules:
        line += 1
        if canHold2(b): c += 1
    return c

def part2(b, nb):
    if rules[b] == 0: return 0
    elif b in p2: return p2[b]
    sg = rules[b].split("&")
    for a in range(len(sg)):
        num = nums[b][a]
        nb += num + (num * part2(sg[a],0))    
    p2[b] = nb
    return nb

print(part1())
print("----%s-----:p1" % (stime - time.perf_counter()))
stime = time.perf_counter()
print(part2("shiny gold",0))
print("----%s-----:p2" % (stime - time.perf_counter()))
print("----%s-----:total" % (ttime - time.perf_counter()))