import time
stime = time.perf_counter()
with open("in9.txt", "r") as f: data = [int(n) for n in f.readlines()]

def preSum(val,preamble):
    for i in preamble:
        for k in range(len(preamble)):
            if i + preamble[-(k+1)]== val:
                if i == preamble[-(k+1)]: continue
                else: return True   
            k -= 1
    return False

def part1(s):
    preamble = data[:s]
    for i in data[s:]:
        if preSum(i,preamble): pass
        else: 
            print(i,"---%s:p1" % ((stime - time.perf_counter())))
            return i
        preamble.pop(0)
        preamble.append(i)

def part2(inval):
    for i in range(len(data)):
        dic = {data[i] : 2}
        lis = [data[i]]
        for t in data[i:]:
            if t in dic: continue
            sval = sum(lis[:]) + t
            if sval == inval:
                print(max(lis) + min(lis),"---%s:p2" % ((stime - time.perf_counter())))
                return True
            elif sval > inval: break
            lis.append(t)
            dic[t] = 1

part2(part1(25))