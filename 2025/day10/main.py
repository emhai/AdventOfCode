import itertools
import os

from docutils.frontend import validate_url_trailing_slash


def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    input = []
    for c in content:
        lights, rest = c.split("]")
        lights = lights[1:]
        buttons, curly = rest.split("{")
        buttons = buttons.strip()
        buttons = buttons.split(" ")
        final_buttons = []
        for b in buttons:
            b = b[1:-1]
            b = b.strip()
            b = b.split(",")
            b = [int(single) for single in b]
            final_buttons.append(b)

        curly = curly[:-1]
        curly = curly.strip()
        curly = curly.split(",")
        curly = [int(single) for single in curly]

        input.append([lights, final_buttons, curly])

    f.close()
    return input

def part_1(content):

    amounts = [10000] * len(content)
    final_combos = [[]] * len(content)
    for j, line in enumerate(content):
        final_lights = line[0]
        buttons = line[1]
        no_buttons = len(buttons)
        combinations = []
        for i in range(1, no_buttons):
            combinations.extend(list(itertools.combinations(buttons, i)))

        for combo in combinations:
            lights = ["."] * len(final_lights)

            for b in combo:
                for num in b:
                    if lights[num] == ".":
                        lights[num] = "#"
                    else:
                        lights[num] = "."

            if "".join(lights) == final_lights:
                if len(combo) < amounts[j]:
                    amounts[j] = len(combo)
                    final_combos[j] = combo
            print("".join(lights))
            print()

    counter = 0
    for a in amounts:
        counter += a

    return counter
def part_2(content):
    amounts = [10000] * len(content)
    final_combos = [[]] * len(content)
    final_joltages = [[]] * len(content)

    for j, line in enumerate(content):
        buttons = line[1]
        final_joltage = line[2]
        repeats = 1

        while True:
            print("repeat", repeats)

            c2 = list(itertools.combinations_with_replacement(buttons, repeats))
            for combo in c2:
                joltage = [0] * len(final_joltage)
                for b in combo:
                    for num in b:
                        joltage[num] += 1


                if joltage == final_joltage:
                    if len(combo) < amounts[j]:
                        amounts[j] = len(combo)
                        final_combos[j] = combo
                        final_joltages[j] = joltage

                    #print()

            if amounts[j] != 10000:
                print("broke")
                break
            repeats += 1

    counter = 0
    for a in amounts:
        counter += a

    return counter


def main():
    content = get_content("input_test.txt")
    # test_1 = part_1(content)
    test_2 = part_2(content)

    content = get_content("input.txt")
    # res_1 = part_1(content)
    res_2 = part_2(content)

    # print("RESULT TEST 1:", test_1)
    # print("RESULT 1:", res_1)
    print("RESULT TEST 2:", test_2)
    print("RESULT 2:", res_2)

if __name__ == '__main__':
    main()
