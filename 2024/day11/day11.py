from os.path import split


def split_stone(stones):

    new_round_stones = []

    for s in range(len(stones)):
        if stones[s] == 0:
            new_round_stones.append(1)
        elif len(str(stones[s])) % 2 == 0:

            string_stone = str(stones[s])
            length = int(len(string_stone)/ 2)

            s1 = string_stone[:length]
            s2 = string_stone[length:]
            new_round_stones.append(int(s1))
            new_round_stones.append(int(s2))
        else:
            new_round_stones.append(stones[s] * 2024)


    return new_round_stones


def level1():

    file = open("day11.txt", "r")
    content = file.read().strip().split()
    stones = [int(x) for x in content]
    full_list = []

    for i in range(75):
        print(i)
        stones = split_stone(stones)
        #print(new_list)

    print(len(stones))


def merge_stone(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

def rec_split_stone(stone, round):

    if round == 75:
        return stone

    list = []
    if stone == 0:
        list.append(rec_split_stone(1, round + 1))
    elif len(str(stone)) % 2 == 0:

        string_stone = str(stone)
        length = int(len(string_stone)/ 2)

        s1 = int(string_stone[:length])
        s2 = int(string_stone[length:])
        list.append(rec_split_stone(int(s1), round + 1))
        list.append(rec_split_stone(int(s2), round + 1))

    else:
        list.append(rec_split_stone(stone * 2024, round + 1))


    return list

def level2():

    file = open("day11.txt", "r")
    content = file.read().strip().split()
    stones = [int(x) for x in content]

    for stone in stones:
        for i in range(3):
            print(i)
            stones = rec_split_stone(stone, 0)
            #print(new_list)
        print(stones)
    print(len(stones))


if __name__ == '__main__':
    #level1()
    level2()