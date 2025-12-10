import itertools
import os

def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    f.close()
    return content

def part_1(content):
    content = [c.split(",") for c in content]
    for i in range(len(content)):
        for j in range(len(content[i])):
            content[i][j] = int(content[i][j])

    combinations = itertools.combinations(content, 2)
    combinations = list(combinations)
    combinations = [list(c) for c in combinations]
    largest_area = 0
    for c in combinations:
        length_horizontal = abs(c[0][0] - c[1][0]) + 1
        length_vertical = abs(c[0][1] - c[1][1]) + 1
        area = length_horizontal * length_vertical
        if area > largest_area:
            largest_area = area

    return largest_area

def print_field(field):
    for f in field:
        row = ""
        for r in f:
            row += r
        print(row)
    print()

def part_2(content):
    content = [c.split(",") for c in content]
    values_w, values_h = [], []
    for i in range(len(content)):
        content[i][0] = int(content[i][0])
        content[i][1] = int(content[i][1])
        values_w.append(content[i][0])
        values_h.append(content[i][1])

    max_w, max_h = max(values_w) + 1, max(values_h) + 1
    print(max_w, max_h)
    combinations = itertools.combinations(content, 2)
    field = []
    for i in range(max_w):
        row = []
        for j in range(max_h):
            row.append(".")
        field.append(row)

    print_field(field)

    content.append(content[0])
    for c in content:
        field[c[0]][c[1]] = "#"

    print_field(field)

    combinations = list(combinations)
    combinations = [list(c) for c in combinations]
    largest_area = 0
    for c in combinations:
        p1, p2 = c[0], c[1]

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
