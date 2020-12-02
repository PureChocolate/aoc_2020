with open("in2.txt", "r") as file:
    data = file.readlines()

def run():
    counter = 0
    counter2= 0
    for i in range(len(data)):
        first = int(data[i][:data[i].find("-")])
        second = int(data[i][data[i].find("-")+1:data[i].find(" ")])
        let = data[i][data[i].find(" ")+1]
        s = data[i][data[i].find(":")+2:]
        if first <= s.count(let) <= second: 
            counter += 1
        if ((s[first-1] == let or s[second-1] == let) and not 
            (s[first-1] == let and s[second-1] == let)) == True:
            counter2 += 1   
    print counter
    print counter2

run()

    






