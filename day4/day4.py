import re
with open("in4.txt", "r") as f:
    # for line in f.readlines():
    #     if line == "\n": bruh += 1
    # data = [] #f.read().split("\n\n")
    data = []
    s = ""
    for line in f.readlines():
        if line == "\n":
            data.append(s.replace("\n","")[:-1])
            s = ""
        else: s += line + " "
    data.append(s.replace("\n","")[:-1])

# for i in range(10):
#     print data[i]
# print len(data)

rules = ["byr", "iyr","eyr","hgt","hcl","ecl","pid","cid"]
clrs = ["amb","blu","brn","gry","grn","hzl","oth"]
c = 0
def dataValid(pars,vals):
    for i in range(len(pars)):
        val = vals[i]
        par = pars[i]
        if par == "ecl" and not val in clrs:
            return False
        if par == "hcl" and val[:1] == "#":
            if all( c in set("abcdef0123456789") for c in val[1:]) and len(val[1:]) == 6:
                return True
            else:
                return False
        if par == "pid":
            if val.isdigit(): 
                if len(val) == 9: 
                    return True
            return False            
        try:
            if par == "hgt":
                if val[-2:] == "in" and not 76 >= int(val[:-2]) >= 59:
                    return False
                elif val[-2:] == "cm" and not 193 >= int(val[:-2]) >= 150:
                    return False
                elif not val[-2:].isalpha():
                    return False
            if par == "byr" and not 2002 >= int(val) >= 1920:
                return False
            if par == "iyr" and not 2020 >= int(val) >= 2010:
                return False
            if par == "eyr" and not 2030 >= int(val) >= 2020:
                return False
        except ValueError:
            return False
    return True

for i in range(len(data)):
    # print "\n"
    test = [s for s in data[i].split()]
    pars = ""
    vals = ""
    for k in range(len(test)):
        pars += test[k].split(":")[0] + " "
        vals += test[k].split(":")[1] + " "
    pars = pars.split()
    vals = vals.split()
    # if(set(pars) == set(rules[:-1])): print "poggers"
    if all(w in pars for w in rules[:7]):
        # print str(pars) + "///////////////"
        # print str(vals) + "$$$$$$$$$$$$$$$"
        if dataValid(pars,vals): c += 1
    # if all(r in data[i] for r in rules[:7]):
        # c += 1
        # test = [ a for a in data[i].split(" ")]
        # if dataValid(test): c += 1 

print c

