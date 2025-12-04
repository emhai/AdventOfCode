def level2():
    file = open("day2.txt", "r")
    color_names = ["red", 'green', "blue"]
    color_values = [0, 0, 0]
    total_power = 0

    for line in file:
        print(line)
        split_line = line.split(":")
        sets = split_line[1].split(";")
        for game_set in sets:
            chunks = game_set.split()
            for i in range(0, len(chunks), 2):
                amount = int(chunks[i])
                name = chunks[i + 1].replace(",", "")
                color_index = color_names.index(name)
                if color_values[color_index] < amount:
                    color_values[color_index] = amount
        power = color_values[0] * color_values[1] * color_values[2]
        total_power += power
        color_values = [0, 0, 0]
    print(total_power)
def level1():
    file = open("day2.txt", "r")
    color_names = ["red", 'green', "blue"]
    color_maxima = [12, 13, 14]
    num_playable_games = 0
    for line in file:
        print(line)
        split_line = line.split(":")
        ID = int(split_line[0].split()[1])

        sets = split_line[1].split(";")
        playable = True
        for game_set in sets:
            chunks = game_set.split()
            for i in range(0, len(chunks), 2):
                amount = int(chunks[i])
                name = chunks[i + 1].replace(",", "")
                color_index = color_names.index(name)
                if amount > color_maxima[color_index]:
                    playable = False
        if playable:
            num_playable_games += ID

    print(num_playable_games)


if __name__ == '__main__':
    #level1()
    level2()
