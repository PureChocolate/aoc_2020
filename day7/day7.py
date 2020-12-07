with open("in7.txt", "r") as f: 
    lr = f.read().strip().replace(" bags contain ","-").replace(" bag, ","-").replace(" bags, ", "-").replace(" bag.", "-").replace(" bags.", "-").split("\n")
rules = {}
bags = []

for t in lr:
    s = ""
    t = t.split("-")[:-1]
    if "no other" in t: rules[t[0]] = "no other"
    else:
        for r in t[1:]: s += ("&" + r)
        rules[t[0]] = s[1:]
    if "shiny gold" in rules[t[0]]: bags.append(t[0])

def canHold2(bag):
    if any(a in rules[bag] for a in bags):
        return True
    elif "no other" in rules[bag]:
        return False
    else:
        for i in rules[bag].split("&"):
            if canHold2(i[2:]): return True

def part1():
    c = 0
    for b in rules:
        if b not in bags:
            if canHold2(b): c += 1
        else: c += 1
    return c

def part2(b, nb):
    if "no other" in rules[b]: return 0
    sg = rules[b].split("&")
    for a in sg:
        num = int(a[0])
        nb += num + num * part2(a[2:],0)
    return nb

print(part1(), part2("shiny gold",0))