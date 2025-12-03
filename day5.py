
def level1():
    file = open("day5.txt", "r")
    seeds = file.readline().split(":")[1].split()
    print(seeds)
    line = file.readline()
    data = [[]]
    for i in range(7):
        line = file.readline()
        print("----------------------------------")
        while True:
            if line == "\n":
                break
            sets = line.split()
            start = sets[0]
            dest = sets[1]
            amount = sets[2]

            line = file.readline()
            print(line)

        print("done1")
    print("done")





def level2():
    return



if __name__ == '__main__':
    level1()
    level2()
