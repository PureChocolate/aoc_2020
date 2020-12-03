with open("in3.txt", "r") as f: m = f.read().splitlines()

def run(r,d):
    y = x = trees = 0
    while(y < len(m)):        
        while(True):
            try: 
                if m[y][x] == "#": trees += 1
                break
            except IndexError: m[y] += m[y]
        x += r
        y += d
    return trees

print run(3,1) * run(1,1) * run (5,1) * run(7,1) * run(1,2)








