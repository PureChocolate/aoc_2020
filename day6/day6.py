with open("in6.txt", "r") as f: qd = [a.strip().split("\n") for a in f.read().split("\n\n")]

s = d = 0
for l in qd:
    track = track0 = ""
    c = 0
    for a in l:
        track += a
        if len(a) > 1:
            for g in a:
                if g not in track0: track0 += g
        elif a not in track0: track0 += a
    for x in track:
        if track.count(x) == len(l):
            c += 1
            track = track.replace(x, "",len(l))
    s += c
    d += len(track0)
print(s, d)

