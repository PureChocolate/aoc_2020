from collections import defaultdict
with open("test.txt","r") as f : data = f.read().strip().split("\n")
mem = defaultdict(lambda: "")
mask = ""
# print(f'{6:08b}')
def run(p1,p2):
    for a in data:
        if a.startswith("mask"): mask = a[7:]
        else:
            add = a[4:].split("]")
            val = mVal = ""
            for a in add: 
                val = a.split(" = ")
                val = val[1:]
            if p1:
                masked = f'{int(val[0]):036b}'
                for v in range(len(mask)):
                    if mask[v] == "X": mVal += masked[v]
                    else: mVal += mask[v]
                mem[add[0]] = mVal
            elif p2:
                xC = 0
                masked = f'{int(add[0]):036b}'
                for v in range(len(mask)):
                    if mask[v] == "X":
                        mVal += "X"
                        xC += 1
                    elif mask[v] == "0":
                        mVal += masked[v]
                    elif mask[v] == "1":
                        mVal += "1"
                print(mVal)
                memAdds = []
                for i in range(2 ** xC):
                    for a in mVal[::-1]: 
                        if a == "X":
                            memAdds.append(a)


    tot = 0
    for a in mem: tot += int(mem[a],2)
    return tot

print(run(False,True))
# print(data)