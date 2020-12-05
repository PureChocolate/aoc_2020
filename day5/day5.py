import math as m
with open("in5.txt", "r") as f: 
    bdata = f.read().split("\n")
    
row = 0
col = 0
seatID = 0
seats = []
for i in range(len(bdata)):
    maxR = 127
    minR = 0
    maxC = 7
    minC = 0
    for a in range(len(bdata[i])):
        if bdata[i][a] == "F":
            if a == 6:
                row = minR
                continue
            maxR = m.floor((maxR + minR)/2.0)
            minR = minR
        elif bdata[i][a] == "B":
            if a == 6:
                row = maxR
                continue
            maxR = maxR
            minR = m.ceil((minR + maxR)/2.0)
        elif bdata[i][a] == "R":
            if a == len(bdata[i])-1:
                col = maxC
                continue
            maxC = maxC
            minC = m.ceil((minC + maxC)/2.0)        
        elif bdata[i][a] == "L":
            if a == len(bdata[i])-1:
                col = minC
                continue
            maxC = m.floor((maxC + minC)/2.0)
            minC = minC
    seats.append(((row * 8) + col))
    if ((row * 8) + col) > seatID : seatID = ((row * 8) + col)

for l in range(len(seats)):
    if l not in seats and  900 > l > 100:
        print l

print seatID