import re

directions = ["left", "up", "right", "down"]
dir_symbols = ["<", "^", ">", "v"]


def find_position(content):
    i = 0
    while 0 <= i < len(content):
        line = content[i]
        j = 0
        while 0 <= j < len(line):
            char = line[j]
            if char == "^":
                return i, j, 1
            if char == "v":
                return i, j, 3
            if char == "<":
                return i, j, 0
            if char == ">":
                return i, j, 2
            j += 1
        i += 1


def level1():
    file = open("day6.txt", "r")

    file_content = file.readlines()
    content = []
    for line in file_content:
        content.append(list(line.strip()))

    height = len(content)
    width = len(content[0])
    i, j, direction = find_position(content)
    content[i][j] = "."

    next_i = i
    next_j = j

    while True:
        if direction == 1:
            next_i = i - 1
            next_j = j
        if direction == 3:
            next_i = i + 1
            next_j = j
        if direction == 0:
            next_i = i
            next_j = j - 1
        if direction == 2:
            next_i = i
            next_j = j + 1

        if next_i < 0 or next_i >= height or next_j < 0 or next_j >= width:
            print("done")
            break

        print(next_i, next_j)
        if content[next_i][next_j] == "." or content[next_i][next_j] == "X":
            content[i][j] = "X"
            i = next_i
            j = next_j

            print(i, j, "moving")
            continue

        if content[next_i][next_j] == "#":
            direction = (direction + 1) % 4
            print(i, j, "turning right", direction)

    sum = 0
    for line in content:
        for char in line:
            if char == "X":
                sum += 1

    print(sum + 1)


def level2():
    file = open("day6.txt", "r")

    file_content = file.readlines()
    content = []
    for line in file_content:
        content.append(list(line.strip()))

    height = len(content)
    width = len(content[0])
    i, j, direction = find_position(content)
    original_i = i
    original_j = j
    original_dir = direction
    content[i][j] = "."

    next_i = i
    next_j = j
    working_obstacles = 0
    copy_content = [row[:] for row in content]

    for obs_i in range(0, height):
        print("row", obs_i)
        for obs_j in range(0, width):
            content = [row[:] for row in copy_content]
            i = original_i
            j = original_j
            direction = original_dir
            if content[obs_i][obs_j] == "#":
                continue

            if obs_i == original_i and obs_j == original_j:
                continue

            content[obs_i][obs_j] = "#"
            already_taken_steps = [[i, j, direction]]
            steps = 0
            counter = 0
            while True:

                if direction == 1:
                    next_i = i - 1
                    next_j = j
                if direction == 3:
                    next_i = i + 1
                    next_j = j
                if direction == 0:
                    next_i = i
                    next_j = j - 1
                if direction == 2:
                    next_i = i
                    next_j = j + 1

                if next_i < 0 or next_i >= height or next_j < 0 or next_j >= width:
                    break

                if content[next_i][next_j] == "." or content[next_i][next_j] == "X":
                    content[i][j] = "X"
                    i = next_i
                    j = next_j
                    this_step = [i, j, direction]
                    if counter % 20 == 0 and this_step in already_taken_steps:
                        working_obstacles += 1
                        print("work")
                        break
                    already_taken_steps.append(this_step)
                    counter += 1
                    continue

                if content[next_i][next_j] == "#":
                    direction = (direction + 1) % 4

                steps += 1

            content[obs_i][obs_j] = "."

    print(working_obstacles)


if __name__ == '__main__':
    # level1()
    level2()
