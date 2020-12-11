import time
stime = time.perf_counter()
with open("big8.txt","r") as f: codes = f.read().strip().split("\n")
print("---%s---:parse" % (stime - time.perf_counter()))

def boot(code):
    acc = i = 0
    ran = set()
    while(True):
        if i in ran:
            return (False,acc)
        else:
            if i >= len(code):
                return (True,acc)
            inst = code[i][0]
            val = int(code[i][4:])
            if "n" == inst:
                ran.add(i)
                i += 1  
            elif "a" == inst:
                ran.add(i)
                acc +=  val
                i += 1
            elif "j" == inst:
                ran.add(i)
                i += val
                continue

print(boot(codes[:]))
print("---%s---:p1" % (stime - time.perf_counter()))

test = (False,0)              
for i in range(len(codes)):
    temp = codes.copy()
    if "nop" in temp[i]:
        temp[i] = "jmp" + temp[i][3:]
        test = boot(temp)
        if test[0]: break
    elif "jmp" in temp[i]:
        temp[i] = "nop" + temp[i][3:]
        test = boot(temp)
        if test[0]: break
        
print(test)
print("---%s---:p2" % (stime - time.perf_counter()))