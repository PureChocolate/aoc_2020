with open("in1.txt", "r") as f:
    values = [int(n) for n in f.readlines()]

found = False
## test
for n in values:
    for a in values:
        for c in values:
            if a + n  + c == 2020: 
                print("viola " + str(a) + " " + str(n) + " " + str(c))
                print(a * n * c)
    if found is True: break
