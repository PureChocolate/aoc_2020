with open("in5.txt", "r") as f: bp = f.read().split("\n")
max = 0
seats = []
for a in bp:
    num = (a.translate(str.maketrans({"B":"1", "F": "0", "R":"1","L":"0"})))
    val = int(num[-3:],2)
    num = int(num[:7],2)
    seats.append((num * 8) + val)
    if (num * 8) + val > max: max = (num * 8) + val
for i in range(len(bp)):
    if i + 1 in seats and i - 1 in seats and i not in seats: print(i)
print(max)