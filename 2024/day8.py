import numpy
import itertools


def level1():
    file = open("day8.txt", "r")
    content = file.read()
    set_of_letters = set(content)
    set_of_letters.remove("\n")
    set_of_letters.remove(".")
    file.seek(0)
    dictionary = {}
    for letter in set_of_letters:
        dictionary[letter] = []

    content = file.readlines()
    height = len(content)
    width = len(content[0].strip())
    edit_content = []

    for i in range(len(content)):
        line = list(content[i].strip())
        edit_content.append(line)
        for j in range(len(line)):
            char = line[j]
            if char == ".":
                continue
            dictionary[char].append([i, j])

    print(dictionary)
    hashtags = []

    for k, v in dictionary.items():

        subset = list(itertools.combinations(v, 2))

        for comb in subset:
            diff = list(numpy.subtract(comb[1], comb[0]))

            antinodes = [list(numpy.subtract(comb[0], diff)), list(numpy.add(comb[1], diff))]
            for antinode in antinodes:
                if antinode[0] < 0 or antinode[0] >= height or antinode[1] < 0 or antinode[1] >= width:
                    continue
                edit_content[antinode[0]][antinode[1]] = "#"

                if antinode not in hashtags:
                    hashtags.append(antinode)

    print(hashtags)
    print(len(hashtags))

def is_outside_bounds(antinode, height, width):
    if antinode[0] < 0 or antinode[0] >= height or antinode[1] < 0 or antinode[1] >= width:
        return True
    else:
        return False

def level2():
    file = open("day8.txt", "r")
    content = file.read()
    set_of_letters = set(content)
    set_of_letters.remove("\n")
    set_of_letters.remove(".")
    file.seek(0)
    dictionary = {}
    for letter in set_of_letters:
        dictionary[letter] = []

    content = file.readlines()
    height = len(content)
    width = len(content[0].strip())
    edit_content = []

    for i in range(len(content)):
        line = list(content[i].strip())
        edit_content.append(line)
        for j in range(len(line)):
            char = line[j]
            if char == ".":
                continue
            dictionary[char].append([i, j])

    print(dictionary)
    hashtags = []

    for k, v in dictionary.items():

        subset = list(itertools.combinations(v, 2))

        for comb in subset:
            diff = list(numpy.subtract(comb[1], comb[0]))

            antinode = list(numpy.subtract(comb[0], diff))
            while not is_outside_bounds(antinode, height, width):

                if edit_content[antinode[0]][antinode[1]] != ".":
                    antinode = list(numpy.subtract(antinode, diff))
                    continue

                edit_content[antinode[0]][antinode[1]] = "#"

                if antinode not in hashtags:
                    hashtags.append(antinode)

                antinode = list(numpy.subtract(antinode, diff))

            antinode = list(numpy.add(comb[1], diff))
            while not is_outside_bounds(antinode, height, width):

                if edit_content[antinode[0]][antinode[1]] != ".":
                    antinode = list(numpy.add(antinode, diff))
                    continue

                edit_content[antinode[0]][antinode[1]] = "#"

                if antinode not in hashtags:
                    hashtags.append(antinode)

                antinode = list(numpy.add(antinode, diff))

        if len(v) > 1:
            for item in v:
                hashtags.append(item)
    print(hashtags)
    print(len(hashtags))


if __name__ == '__main__':
    level1()
    level2()
