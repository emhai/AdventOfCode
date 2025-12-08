import copy
import os

def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    content = [list(i) for i in content]
    f.close()
    return content

def part_1(content):

    splits = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if i + 1 >= len(content):
                continue
            if content[i][j] == "S" or content[i][j] == "|":
                if content[i + 1][j] == ".":
                    content[i + 1][j] = "|"
                elif content[i + 1][j] == "^":
                    splits += 1
                    content[i + 1][j + 1] = "|"
                    content[i + 1][j - 1] = "|"

    print(content)
    return splits

def part_2(content):

    splits = 0
    for i in range(0, len(content)):
        for j in range(len(content[i])):
            if content[i][j] == ".":
                content[i][j] = 0

    for i in range(len(content)):
        for j in range(len(content[i])):
            if i + 1 >= len(content):
                continue

            if content[i][j] == "S":
                content[i + 1][j] = 1
                continue

            if content[i][j] == "^":
                continue

            if content[i + 1][j] == "^":
                content[i + 1][j + 1] += content[i][j]
                content[i + 1][j - 1] += content[i][j]
            else:
                content[i + 1][j] += content[i][j]

    splits = 0
    for num in content[-1]:
        splits += num
    return splits

def main():

    content = get_content("input_test.txt")
    content_1 = copy.deepcopy(content)
    content_2 = copy.deepcopy(content)
    test_1 = part_1(content_1)
    test_2 = part_2(content_2)

    content = get_content("input.txt")
    content_1 = copy.deepcopy(content)
    content_2 = copy.deepcopy(content)
    res_1 = part_1(content_1)
    res_2 = part_2(content_2)

    print("RESULT TEST 1:", test_1)
    print("RESULT 1:", res_1)
    print("RESULT TEST 2:", test_2)
    print("RESULT 2:", res_2)

if __name__ == '__main__':
    main()
