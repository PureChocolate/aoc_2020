import time
with open("in1.txt", "r") as f: values = [int(n) for n in f.readlines()]

stime = time.time()

def run(val):
    values.sort()
    for g in range(len(values)):
        r = len(values) - 1
        l = g + 1
        while l < r:
            s = values[l] + values[r] + values[g]
            if s == val: return values[l] * values[r] * values[g]
            elif s > val: r -= 1            
            else: l += 1

    # for n in values:
    #     for a in values:
    #         for c in values:
    #             if a + n  + c == 2020: 
    #                 print("viola " + str(a) + " " + str(n) + " " + str(c))
    #                 return a * n * c

print(run(2020))
print("---%s---" % ((time.time() - stime) * 1000))