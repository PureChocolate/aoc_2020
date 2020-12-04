with open("in4.txt", "r") as f:
    data = []
    s = ""
    for line in f.readlines():
        if line == "\n":
            data.append(s.replace("\n","")[:-1])
            s = ""
        else: s += line + " "
    data.append(s.replace("\n","")[:-1])

rules = ["byr", "iyr","eyr","hgt","hcl","ecl","pid","cid"]
clrs = ["amb","blu","brn","gry","grn","hzl","oth"]
c = 0
def dataValid(temp):
    for i in range(len(temp)):
        temp[i] = temp[i].split(":")
        val = temp[i][1]
        par = temp[i][0]
        if par == "ecl" and not val in clrs: 
            return False
        if par == "hcl" and not val[:1] == "#": 
            if not val[1:].isalnum() or not len(val[1:]) == 6:
                return False
        if par == "pid" and not len(val) == 9:
            return False
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
    return True


for i in range(len(data)):
    if all(r in data[i] for r in rules[:7]):
        test = [ a for a in data[i].split(" ")]
        if dataValid(test): c += 1 

print c

