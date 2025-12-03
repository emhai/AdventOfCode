import math

import numpy as np

directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def check_connected_region(field, pos_i, pos_j, already_reached):

    already_reached.append([pos_i, pos_j])
    height = len(field)
    width = len(field[0])

    for direction in directions:
        new_i = pos_i + direction[0]
        new_j = pos_j + direction[1]

        if new_i < 0 or new_i >= height or new_j < 0 or new_j >= width:
            continue

        if [new_i, new_j] in already_reached:
            continue

        plant = field[pos_i][pos_j]
        new_plant = field[new_i][new_j]
        if new_plant != plant:
            continue

        check_connected_region(field, new_i, new_j, already_reached)

    return

def level1():

    file = open("day12.txt", "r")
    content = file.readlines()
    field = []
    for line in content:
        field.append(line.strip())

    height = len(field)
    width = len(field[0])
    total_already_reached = []
    connected_regions = []

    for i in range(height):
        for j in range(width):
            if [i, j] in total_already_reached:
                continue
            already_reached = []
            check_connected_region(field, i, j, already_reached)
            connected_regions.append(already_reached)
            for pos in already_reached:
                total_already_reached.append(pos)

    print(connected_regions)
    print(len(total_already_reached))
    print(len(connected_regions))

    cost = 0
    for region in connected_regions:
        circumference = 0
        for patch in region:

            for direction in directions:
                new_i = patch[0] + direction[0]
                new_j = patch[1] + direction[1]

                if new_i < 0 or new_i >= height or new_j < 0 or new_j >= width:
                    circumference += 1
                    continue

                plant = field[patch[0]][patch[1]]
                new_plant = field[new_i][new_j]

                if new_plant != plant:
                    circumference += 1
        cost += circumference * len(region)

    print(cost)

def level2():

    file = open("day12.txt", "r")
    content = file.readlines()

    field = []
    for line in content:
        field.append(line.strip())

    height = len(field)
    width = len(field[0])
    total_already_reached = []
    connected_regions = []

    for i in range(height):
        for j in range(width):
            if [i, j] in total_already_reached:
                continue
            already_reached = []
            check_connected_region(field, i, j, already_reached)
            connected_regions.append(already_reached)
            for pos in already_reached:
                total_already_reached.append(pos)

    print(connected_regions)
    print(len(total_already_reached))
    print(len(connected_regions))

    cost = 0
    for region in connected_regions:
        print("Checking region", field[region[0][0]][region[0][1]])
        print_content = []
        for pr in field:
            print_content.append(list(pr))

        circumferences = []
        circ_plants = []
        for patch in region:

            for direction in directions:
                new_i = patch[0] + direction[0]
                new_j = patch[1] + direction[1]

                if new_i < 0 or new_i >= height or new_j < 0 or new_j >= width:

                    circumferences.append([new_i, new_j])
                    circ_plants.append([patch[0], patch[1]])
                    continue

                plant = field[patch[0]][patch[1]]
                new_plant = field[new_i][new_j]

                if new_plant != plant:
                    circ_plants.append([patch[0], patch[1]])
                    circumferences.append([new_i, new_j])



        sides = 0
        i = len(circumferences) - 1
        #print(circumferences)
        #for l in print_content:
            #print(l)

        while i >= 0:
            #print(circumferences)

            if i != (len(circumferences) - 1):
                print("?")

            checking_field = circumferences[i]
            old_plant = circ_plants[i]

            for direction in directions:
                circ_plants[i] = old_plant
                new_i = circumferences[i][0] + direction[0]
                new_j = circumferences[i][1] + direction[1]
                while [new_i, new_j] in circumferences:
                    distance = math.dist(circ_plants[i], [new_i, new_j])
                    if distance > 2:
                        break
                    index = circumferences.index([new_i, new_j])
                    circumferences.pop(index)
                    circ_plants.pop(index)
                    i -= 1
                    new_i += direction[0]
                    new_j += direction[1]
                    circ_plants[i][0] += direction[0]
                    circ_plants[i][1] += direction[1]

            circumferences.pop(-1)
            circ_plants.pop(-1)
            i -= 1
            sides += 1


        print(sides, "+", len(region), "=", cost)
        cost += sides * len(region)



    print(cost)


if __name__ == '__main__':
    #level1()
    level2()