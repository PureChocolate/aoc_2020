from collections import defaultdict
with open("in11.txt","r") as f: 
    grids = defaultdict(lambda: "0")
    ship = []
    for line in f.readlines():
        ro = []
        for x in line:
            if x == "\n": continue
            # if x == ".": ro.append(x)
            else: ro.append(x)
        ship.append(ro)
for y in range(len(ship)):
    for x in range(len(ship[y])):
        grids[(y,x)] = ship[y][x]

def show(xG):
    c = 0
    for r in range(len(ship)):
        for s in range(len(ship[r])):
            # print(xG[(r,s)], end="")
            if xG[(r,s)] == "#": c += 1
        # print()
    return c

temp = grids.copy()
change = True

def checkAdj(grid,r,s,v):
    vals = ["L","#"]
    totS = 0
    occuS = 0
    emptyS = 0
    a = 1
    # points = [(r-1,s),(r+1,s),(r+1,s+1),(r-1,s-1),(r-1,s+1),(r+1,s-1),(r,s-1),(r,s+1)]
    points = [(r-a,s),(r+a,s),(r+a,s+a),(r-a,s-a),(r-a,s+a),(r+a,s-a),(r,s-a),(r,s+a)]
    for x in range(len(points)):
        a = 1
        for i in range(len(ship[0])):
            points = [(r-a,s),(r+a,s),(r+a,s+a),(r-a,s-a),(r-a,s+a),(r+a,s-a),(r,s-a),(r,s+a)]
            if grid[points[x]] in vals:
                totS += 1
                if grid[points[x]] is vals[1]: 
                    occuS += 1
                    break
                elif grid[points[x]] is vals[0]: 
                    emptyS += 1
                    break
            elif grid[points[x]] is 0: break
            a += 1
    if v == "L":
        if emptyS == totS:
            temp[(r,s)] = "#"
            return 1

    elif v == "#":
        if occuS >= 5:
            temp[(r,s)] = "L"
            return 1
    return 0
    

def run():
    global grids
    change = 0
    for r in range(len(ship)):
        for s in range(len(ship[r])):
            if grids[(r,s)] == ".": continue              
            if grids[(r,s)] == "L":
                change += checkAdj(grids,r,s,"L")
            elif grids[(r,s)] == "#":
                change += checkAdj(grids,r,s,"#")
    grids = temp.copy()
    if(change > 0): return True
    else: return False

while(change):
    # show(grids)
    change = run()
    # print("--------")
print(show(grids))
