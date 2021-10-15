import math
with open("test.txt","r") as f : data = f.readlines()
data[0] = data[0].replace("\n","")
time = int(data[0])
data[1] = data[1].split(",")
buses = []
for a in data[1]:
    if a is not "x":
        buses.append(int(a))
for q in range(len(data[1])):
    if data[1][q] is not "x":
        data[1][q] = int(data[1][q])

ariv = []

for x in buses:
    if x * round(time/x) >= time:
        ariv.append(((x* round(time/x)),x))
    elif x * round(time/x) < time:
        ariv.append(((x * round(time/x)) + x,x))      

# print(time,buses)
# print(ariv)
print((min(ariv)[0] - time) * min(ariv)[1])
example = []
for a in data[1]:
    if a == "x": example.append(".")
    else: example.append(a)
print(example)
track = []
t = 0
# print(type(6/7))
while(True):
    track = []
    hit = False
    for a in range(len(data[1])):
        if type(data[1][a]) == int:
            if t % data[1][a] == 0:
                track.append(data[1][a])
        else: track.append(".")
            
        # if a  == len(data[1]) -1:
        #     track.append(("."))
        t += 1
    t -= len(data[1])
    # if len(track) == len(example)-1:
    #     for a in range(len(data[1])):
    #         if type(data[1][a]) == int:
    #             if t % data[1][a] == 0:
    #                 hit = True
    #                 hold = data[1][a]
    #         if a  == len(data[1]) -1 and not hit:
    #             # print("POGGG")
    #             track.append(".")
    #             break
    #     track.append(hold)
    # if t >= 1068786:
        # print(hit,t,track,hold

    if track == example:
        # print(example,track)
        print(t,track,"huzz")
        break

    # for i in range(len(data[1])):
    #     track.append(data[i])
    if t >= 1068774: 
        print(t,track)
        if t == 1068788:
            print(t,track)
            break
    t += 1
# def compare(a,b):
#     return len(a) == len(b) and len(a) == sum([1 for i,j in zip(a,b) if i ==j])
# print(track)
# print(track == example)
# print(compare(example,track))