with open("in2.txt", "r") as file: data = file.readlines()
    
p1 = p2 = 0
for a in data:
    f,s = map(int, a.split()[0].split("-"))
    l,p = a.split()[1:]; l = l[:1]
    if f <= p.count(l) <= s: p1 += 1
    if ((l in (p[f-1], p[s-1])) and not (p[f-1] == p[s-1] == l)): p2 += 1   

print p1,p2

    






