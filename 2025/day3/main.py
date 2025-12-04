import os

def get_content(file_name):
    f = open(file_name)
    content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    return content

def part_1(content):
    sum = 0
    for line in content:
        max_no_1 = max(line[:-1])
        index_max_no_1 = line.index(max_no_1)
        max_no_2 = max(line[index_max_no_1 + 1:])
        final_no = int(str(max_no_1) + str(max_no_2))
        sum += final_no

    return sum


def part_2(content):

    sum = 0
    for line in content:
        maxs = []
        index_to_beat = -1
        for i in range(11, 0, -1):
            line_subsection = line[index_to_beat + 1: (i * -1)]
            max1 = max(line_subsection)
            index_to_beat = line_subsection.index(max1) + index_to_beat + 1
            maxs.append(max1)

        maxs.append(max(line[index_to_beat + 1:]))
        string_no = ""
        for s in maxs:
            string_no += s
        no = int(string_no)
        sum += no

    return sum


def main():
    content = get_content("input_test.txt")
    test_1 = part_1(content)
    test_2 = part_2(content)

    content = get_content("input.txt")
    res_1 = part_1(content)
    res_2 = part_2(content)

    print("RESULT TEST 1:", test_1)
    print("RESULT 1:", res_1)
    print("RESULT TEST 2:", test_2)
    print("RESULT 2:", res_2)

if __name__ == '__main__':
    main()

