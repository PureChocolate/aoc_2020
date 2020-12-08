with open("in8","r") as f: codes = f.read().split("\n")

def boot(code):
    acc = i = 0
    while(True):
        try:
            if "nop" in code[i]: 
                code[i] += " Checked"        
            elif "acc" in code[i]:
                acc += int(code[i][4:])
                code[i] += " Checked"
            elif "jmp" in code[i]:
                m = int(code[i][3:])
                code[i] += " Checked"
                i += m
                continue
            else: return (True, acc)
        except ValueError:
                return (False,acc)
        i += 1

test = (False,0)              
for i in range(len(codes)):
    temp = codes[:]
    if "nop" in codes[i]:
        temp[i] = "jmp" + temp[i][3:]
        test = boot(temp)
        if test[0]: break
    elif "jmp" in codes[i]:
        temp[i] = "nop" + temp[i][3:]
        test = boot(temp)
        if test[0]: break
        
print(test[1])