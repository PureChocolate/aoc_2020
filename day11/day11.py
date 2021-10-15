from collections import defaultdict
with open("test.txt","r") as f: 
    grids = defaultdict(lambda: "0")
    ship = []
    for line in f.readlines():
        ro = []
        for x in line:
            if x == "\n": continue
            if x == ".": ro.append(x)
            else: ro.append("L")
        ship.append(ro)
for y in range(len(ship)):
    for x in range(len(ship[y])):
        grids[(y,x)] = ship[y][x]
# print((1,2) == (1,3))
def show(xG):
    c = 0
    for r in range(len(ship)):
        for s in range(len(ship[r])):
            print(xG[(r,s)], end="")
            if xG[(r,s)] == "#": c += 1
        print()
    return c

temp = grids.copy()

def checkAdj(grid,r,s,v):
    # print(grid[(r,s-1)],grid[(r,s)],grid[(r,s+1)])
    # print(grid[(r+1,s-1)],grid[(r+1,s)],grid[(r+1,s+1)])
    vals = ["L","#"]
    osm = 0
    os = 0
    a = 1
    # points = [(r-1,s),(r+1,s),(r+1,s+1),(r-1,s-1),(r-1,s+1),(r+1,s-1),(r,s-1),(r,s+1)]
    points2 = [(r-a,s),(r+a,s),(r+a,s+a),(r-a,s-a),(r-a,s+a),(r+a,s-a),(r,s-a),(r,s+a)]
    for x in range(len(points2)):
        # print("----------------")
        # if grid[points2[x]] not in vals:
        #     osm -= 1
        # elif 
        if grid[points2[x]] in vals:
            osm += 1
            if grid[points2[x]] == v:
                os += 1
        # else:
        store = ""
        hit = False
        # print()
        # e = 0
        # while(e < len(ship)+len(ship[0])):
        #     points2 = [(r-a,s),(r+a,s),(r+a,s+a),(r-a,s-a),(r-a,s+a),(r+a,s-a),(r,s-a),(r,s+a)]
        #     store += grid[points2[x]]
        #     # print(grid[points2[x]], points2[x], r,a,(r-a,s),"wwwwww")
        #     # print(points[x] == points2[x],end ="")
        #     if grid[points2[x]] in vals:
        #         # print("eeeeeeeeeee")
        #         osm += 1
        #         if grid[points2[x]] == v:                    
        #             # print("wAAAAA")
        #             os += 1
        #             hit = True
        #             break
        #     elif points2[x][0] == (len(ship))-1 or len(ship[0])-1 == points2[x][1]:
        #         break
        #     elif grid[points2[x]] == "0":
        #         break
        #     a += 1
        #     e += 1
        # if hit: osm -= 1
        # print()
    # print(osm)
    if v == "L":
        # print("poh")
        if os == osm:
            temp[(r,s)] = "#"
            # print("poh")
    elif v == "#":
        if os >= 5:
            temp[(r,s)] = "L"

def run():      
    global grids     
    for r in range(len(ship)):
        for s in range(len(ship[r])):
            if grids[(r,s)] == ".": continue              
            if grids[(r,s)] == "L":
                checkAdj(grids,r,s,"L")
            elif ship[r][s] == "#":
                checkAdj(grids,r,s,"#")
    sItems = {k: temp[k] for k in temp if k in grids and temp[k] == grids[k]}
    grids = temp.copy()
    # if len(sItems) == len(grids):
    #     return 0
show(grids)
print("------")
# checkAdj(grids,0,2,"L")
         
run()
show(grids)
# # # grids[(4,3)] = "L"
# show(grids)
print("------")
run()
show(grids)
print("------")
# run()
# print("------")
# show(grids)
# checkAdj(grids,0,2,"#")
# print(temp[(0,2)])
# show(grids)
# for i in range(len(ship)):
#     for j in range(len(ship[0])):
#         if grids[(i,j)] == "#":
#             checkAdj(grids,i,j,"#")
#         elif grids[(i,j)] == "L":
#             checkAdj(grids,i,j,"L")
# checkAdj(grids,0,3,"L")
# print("--------------")
# for i in range(len(ship)):
#     for j in range(len(ship[0])):
#         print(temp[(i,j)],end="")
#     print()
# print(temp[(0,2)])#,temp[(0,3)])

# run()
# print("-----")
# show(temp)
# print("_____----")
# run(grids)
# show(grids)
# occ = er = 0
# while(er < 2):
#     print("---------")
#     show(grids)
#     print("---555555555------")
#     f = run()
#     occ = show(grids)
#     temp = grids.copy()
#     # if f: break
#     er += 1
# print(occ)