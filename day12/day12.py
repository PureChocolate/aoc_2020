with open("input.txt", "r") as f: inst = f.read().strip().split("\n")
east = north = west = south = 0
ways = ["E", "S", "W", "N"]
wp = [10,0,0,1]
shippos = [0,0,0,0]
facing = ways[0]

for x in inst:
    val = int(x[1:])
    if x[0] == "F":
        # shippos[ways.index(facing)] += val ---- Part 1
        for a in range(4):
            shippos[a] += val*wp[a]
    elif x[0] == "R":
        # r = (ways.index(facing) + int(val/90))%4
        r = int(val/90)%4
        # facing = ways[r]
        # Part1
        for a in range(r):
            b = wp.pop()
            wp.insert(0,b)
    elif x[0] == "L":
        r = int(val/90)%4
        for a in range(r):
            b = wp.pop(0)
            wp.append(b)
    else: 
        wp[ways.index(x[0])] += val
print(wp)
print(shippos[0],shippos[1],shippos[2],shippos[3])
print(abs(shippos[0] - shippos[2])+ abs(shippos[1] - shippos[3]))