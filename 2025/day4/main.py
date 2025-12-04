import copy
import os

from uaclient.api.u.apt_news.current_news.v1 import current_news


def get_content(file_name):
    f = open(file_name)
    content = f.readlines()
    content = [i.replace('\n', '') for i in content]
    content = [list(i) for i in content]
    f.close()
    return content

def part_1(content):

    positions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    height = len(content)
    width = len(content[0])
    counter = 0
    for i in range(height):
        for j in range(width):
            character = content[i][j]
            print(character)
            if character == '.':
                continue
            paper_counter = 0
            for pos in positions:
                new_height = i + pos[0]
                new_width = j + pos[1]
                if 0 <= new_height < height and 0 <= new_width < width:
                    check_character = content[new_height][new_width]
                    if check_character == '@' or check_character == 'x':
                        paper_counter += 1

            if paper_counter < 4:
                content[i][j] = "x"
                counter += 1


    return counter

def part_2(content):
    positions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    height = len(content)
    width = len(content[0])
    counter = 0
    previous_board = None
    while content != previous_board:
        previous_board = copy.deepcopy(content)
        for i in range(height):
            for j in range(width):
                character = content[i][j]
                if character == '.':
                    continue

                paper_counter = 0
                for pos in positions:
                    new_height = i + pos[0]
                    new_width = j + pos[1]
                    if 0 <= new_height < height and 0 <= new_width < width:
                        check_character = content[new_height][new_width]
                        if check_character == '@' or check_character == 'x':
                            paper_counter += 1

                if paper_counter < 4:
                    content[i][j] = "x"
                    counter += 1

        for i in range(height):
            for j in range(width):
                if content[i][j] == 'x':
                    content[i][j] = "."

    print(counter)
    return

def main():
    content = get_content("input.txt")
    # content = get_content("input_test.txt")
    print(part_1(content))
    print(part_2(content))

if __name__ == '__main__':
    main()
