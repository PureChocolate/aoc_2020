from collections import defaultdict
with open("test.txt","r") as f: 
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
            print(xG[(r,s)], end="")
            if xG[(r,s)] == "#": c += 1
        print()
    return c

temp = grids.copy()
change = True

def checkAdj(grid,r,s,v):
    # print(grid[(r,s-1)],grid[(r,s)] +"x",grid[(r,s+1)])
    # print(grid[(r+1,s-1)],grid[(r+1,s)],grid[(r+1,s+1)])
    vals = ["L","#"]
    totS = 0
    occuS = 0
    emptyS = 0
    a = 1
    # points = [(r-1,s),(r+1,s),(r+1,s+1),(r-1,s-1),(r-1,s+1),(r+1,s-1),(r,s-1),(r,s+1)]
    points = [(r-a,s),(r+a,s),(r+a,s+a),(r-a,s-a),(r-a,s+a),(r+a,s-a),(r,s-a),(r,s+a)]
    for x in points:
        a = 1
        for i in range(len(ship[0])):
            print(grid[x] +  ": "+ str(x),end=", ")
            if grid[x] in vals:
                totS += 1
                if grid[x] is vals[1]: 
                    occuS += 1
                    break
                elif grid[x] is vals[0]: 
                    emptyS += 1
                    break
            elif grid[x] is 0: break
            a += 1
        print()
    if v == "L":
        if emptyS == totS: #os == osm:
            temp[(r,s)] = "#"
            return 1
            # print("

    elif v == "#":
        # print(occuS, totS, emptyS)
        if occuS >= 5:
            temp[(r,s)] = "L"
            # print("changed L")
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
    # sItems = {k: temp[k] for k in temp if k in grids and temp[k] == grids[k]}
    grids = temp.copy()
    if(change > 0): return True
    else: return False
    # if len(sItems) == len(grids):
    #     return 0

# while(change):
#     show(grids)
#     change = run()
#     print("--------")
# print(show(grids))
print("----------------")    
show(grids)
k = 5
d = 7
l = 1
c = [(k-l,d),(k+l,d),(k,d-l),(k,d+l)]
for u in c:
    print(u)
l += 1
print("----------------")    
# print(c[0])
for u in c:
    
    print(u)
# checkAdj(grids,4,3,"L")
# run()
print("----------------")  
# show(grids)
# # # grids[(4,3)] = "L"
# checkAdj(grids,0,2,"#")
# show(grids)
# print("----------------")
# run()
# show(temp)
#------------------print("------")
