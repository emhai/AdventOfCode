import sys


def level2():
    sys.setrecursionlimit(2000)
    file = open("day4.txt", "r")

    total_points = 0
    data = []
    for line in file:
        card = line.split(":")[1].split("|")
        winning_nums = card[0].split()
        guess_nums = card[1].split()
        winning_nums.sort()
        guess_nums.sort()
        # print(winning_nums, guess_nums)
        data.append(check_for_win([winning_nums, guess_nums]))
    print(data)
    processed_data = [1] * len(data)
    print(processed_data)
    for i in range(len(data)):
        for k in range(processed_data[i]):
            for j in range(data[i]):
                processed_data[i + j + 1] += 1

        print(processed_data)
    #for card in range(len(data)):
    #    total_points += process_card(card, data)

    print(sum(processed_data))


def process_card(id, data):

    found = check_for_win(data[id])
    if found == 0:
        return 1
    else:
        for i in range(found):
            process_card(id + i, data)


def check_for_win(card):
    winning_nums = card[0]
    guess_nums = card[1]
    i = 0
    j = 0
    found = 0
    while i < len(winning_nums) and j < len(guess_nums):
        if winning_nums[i] == guess_nums[j]:
            found += 1
            i += 1
            j += 1
        elif winning_nums[i] < guess_nums[j]:
            i += 1
        else:
            j += 1

    return found

def level1():
    file = open("day4.txt", "r")

    total_points = 0
    for line in file:
        card = line.split(":")[1].split("|")
        winning_nums = card[0].split()
        guess_nums = card[1].split()
        winning_nums.sort()
        guess_nums.sort()

        found = check_for_win([winning_nums, guess_nums])
        if found == 0:
            continue

        found = pow(2, found - 1)
        total_points += found

    print(total_points)


if __name__ == '__main__':
    level1()
    level2()
