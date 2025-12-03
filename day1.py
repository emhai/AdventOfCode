# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def level1():
    file = open("day1.txt", "r")
    total_sum = 0
    for line in file:
        num = 0
        for c in line:
            if c.isnumeric():
                num = c
                break
        for c in reversed(line):
            if c.isnumeric():
                num += c
                break
        total_sum += int(num)
    print(total_sum)


def find_substring(string):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lowest_index = 100000
    highest_index = 0
    lowest_num = 0
    highest_num = 0

    for num in numbers:
        l_index = string.find(num)
        h_index = string.rfind(num)
        if l_index == -1:
            continue
        if l_index < lowest_index:
            lowest_index = l_index
            lowest_num = numbers.index(num) + 1
        if h_index > highest_index:
            highest_index = h_index
            highest_num = numbers.index(num) + 1

    return [lowest_index, lowest_num, highest_index, highest_num]


def level2():
    file = open("day1.txt", "r")

    total_sum = 0

    for line in file:
        line_length = len(line)
        [lowest_index, lowest_num, highest_index, highest_num] = find_substring(line)

        for index in range(line_length):
            if line[index].isnumeric():
                if index <= lowest_index:
                    lowest_num = line[index]
                break

        for index in range(line_length - 1, -1, -1):
            if line[index].isnumeric():
                if index >= highest_index:
                    highest_num = line[index]
                break

        num = 10 * int(lowest_num) + int(highest_num)
        total_sum += num

    print(total_sum)

if __name__ == '__main__':
    level1()
    level2()
