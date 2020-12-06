import re
import time
stime = time.time()
with open("bigboy.txt", "r") as f: data = f.read().split("\n\n")

rules = ["byr", "iyr","eyr","hgt","hcl","ecl","pid","cid"]
clrs = ["amb","blu","brn","gry","grn","hzl","oth"]

def dataValid(pars,vals):
    for i in range(len(pars)):
        val = vals[i]
        par = pars[i]
        try:
            if par == "ecl" and not val.lower() in clrs: return False
            if par == "hcl" and not re.match(r'^#[0-9A-Fa-f]{6}$', val): return False
            if par == "pid" and not re.match(r'^[0-9]{9}$', val): return False
            if par == "hgt":
                if val[-2:] == "in" and not 76 >= int(val[:-2]) >= 59:
                    return False
                elif val[-2:] == "cm" and not 193 >= int(val[:-2]) >= 150:
                    return False
                elif val[-2:] not in ["in", "cm"]:
                    return False
            if par == "byr" and not 2002 >= int(val) >= 1920: return False
            if par == "iyr" and not 2020 >= int(val) >= 2010: return False
            if par == "eyr" and not 2030 >= int(val) >= 2020: return False
        except ValueError: return False
    return True

c1 = c = 0

for i in range(len(data)):
    test = [s for s in data[i].split()]
    pars = vals = ""
    for k in range(len(test)):
        pars += test[k].split(":")[0] + " "
        vals += test[k].split(":")[1] + " "
    pars = pars.split()
    vals = vals.split()
    if all(w in pars for w in rules[:7]):
        c1 += 1
        if dataValid(pars,vals): c += 1

print(c, c1)
print("---%s---" % ((time.time() - stime)))

