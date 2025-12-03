# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def level1():
    file = open("input2025.txt", "r")
    sum = 0
    for line in file.readlines():
        line = line.replace("\n", "")
        max_no_1 = max(line[:-1])
        index_max_no_1 = line.index(max_no_1)
        max_no_2 = max(line[index_max_no_1 + 1:])
        final_no = int(str(max_no_1) + str(max_no_2))
        print(final_no)
        sum += final_no

    print(sum)



def level2():
    file = open("input2025.txt", "r")
    sum = 0
    for line in file.readlines():
        line = line.replace("\n", "")
        maxs = []
        index_to_beat = -1
        for i in range(11, 0, -1):
            line_subsection = line[index_to_beat + 1: (i*-1)]
            max1 = max(line_subsection)
            index_to_beat = line_subsection.index(max1) + index_to_beat + 1
            maxs.append(max1)

        maxs.append(max(line[index_to_beat + 1:]))
        string_no = ""
        for s in maxs:
            string_no += s
        no = int(string_no)
        print(no)
        sum += no

    print(sum)

if __name__ == '__main__':
    level1()
    level2()
