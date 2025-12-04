import math

import numpy
import itertools


def level1():
    file = open("day9.txt", "r")
    content = file.read().strip()

    line = []
    counter = 0
    mod_counter = 0
    char_counter = 0
    for char in content:
        if mod_counter % 2 == 0:
            for i in range(int(char)):
                line.append(counter)
                char_counter += 1

            counter += 1
        else:
            line += "." * int(char)
        mod_counter += 1


    print(line)
    print(char_counter)
    string_line = line
    line = list(line)
    line2 = ""
    char_counter2 = 0

    for i in range(len(line) - 1, 0, -1):
        print(char_counter2, "/", char_counter)
        if char_counter == char_counter2:
            break
        if line[i] == '.':
            line.pop(i)
            continue

        num_to_sort = line[i]
        for j in range(len(line)):
            if line[j] == ".":
                line[j] = num_to_sort
                line.pop(i)
                char_counter2 += 1
                break


    print(line)
    diff = len(line) - len(line2)
    line2 += "." * diff
    print(line2)

    sum = 0
    mul_counter = 0
    for char in line:
        if char == ".":
            break
        sum += mul_counter * int(char)
        mul_counter += 1


def level2():
    file = open("day9.txt", "r")
    content = file.read().strip()

    line = []
    dict_len = []

    counter = 0
    mod_counter = 0
    for char in content:
        if mod_counter % 2 == 0:
            small_line = ""
            dict_len[counter] = int(char)
            for i in range(int(char)):
                small_line += str(counter)

            line.append(small_line)
            counter += 1
        else:
            line += "." * int(char)
        mod_counter += 1

    print(line)
    string_line = "".join(line)


    i = len(line) - 1
    string_i = len(string_line) - 1


    while i >= 0:
        if line[i] == ".":
            i -= 1
            string_i -= 1
            continue
        #if i % 100 == 0:
        #print("i", i)
        #print("string_i", string_i)
        #print(string_line)

        num_to_sort = line[i]
        length_num = len(num_to_sort)
        space_to_find = "." * length_num
        #print(num_to_sort)
        #index_num = string_line.rfind(num_to_sort)
        index_num = string_i
        index = string_line[:index_num + 1].find(space_to_find)
        if index == -1:
            string_i -= length_num
            i -= 1
            continue

        list_string_line = list(string_line)

        for pop in range(length_num):
            list_string_line[index + pop] = num_to_sort[pop]
            list_string_line[index_num - pop] = "."

        string_line = "".join(list_string_line)
        i -= 1
        string_i -= length_num

    print(string_line)
    sum = 0
    mul_counter = 0
    for char in string_line:
        if char == ".":
            mul_counter += 1
            continue
        sum += mul_counter * int(char)
        mul_counter += 1

    print(sum)
if __name__ == '__main__':
    #level1()
    level2()
