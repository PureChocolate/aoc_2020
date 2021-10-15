import numpy as np
with open("input.txt", "r") as f: inst = f.read().strip().split("\n")
east = north = west = south = 0
# dirs ={0: east, 90: north, 180: west, 270: south}
ways = ["E", "S", "W", "N"]
wp = [10,0,0,1]
shippos = [0,0,0,0]
# for p in range(4):
#     shippos[p] += 10*wp[p]   
# print(shippos)
# print(np.roll(wp,1))
# for i in range(3*4):
#     wp.insert(0,(wp.pop()))
# print(wp)
# wp = [10,0,0,1]
facing = ways[0]
for x in inst:
    # print(east,west,north,south,facing, x[0])
    val = int(x[1:])
    r = (ways.index(facing) + int(val/90))%4
    if x[0] == "F":
        if facing == "E":
            east += val
        elif facing == "S": 
            south += val
        elif facing == "W":
            west += val
        elif facing == "N":
            north += val
        for p in range(4):
            # print(val*wp[p])
            shippos[p] += val*wp[p]        
    elif x[0] == "N":
        north += val
        wp[3] += val
    elif x[0] == "S": 
        wp[1] += val
        south += val
    elif x[0] == "E": 
        wp[0] += val
        east += val
    elif x[0] == "W": 
        wp[2] += val
        west += val
    elif x[0] == "R":
        r = (ways.index(facing) + int(val/90))%4
        facing = ways[r]
        for i in range(3*(r)):
            wp.append(wp.pop(0))
        # print("aaaa",wp)
    elif x[0] == "L":
        r = (int(val/90))%4
        facing = ways[ways.index(facing)-r]
        for i in range(3*(r)):
            wp.insert(0,wp.pop())
        # print("bbbb")
    # print(shippos,wp)
    
    # print(east,west,north,south,facing)
print(wp)
print(shippos[0],shippos[1],shippos[2],shippos[3])
print(abs(shippos[0] - shippos[2])+ abs(shippos[1] - shippos[3]))
print(abs(east-west) + abs(north-south))
# print(east,north)
# print(abs(east) + abs(north))




# print(inst)