import copy
import os

def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    input = {}
    for c in content:
        device, outs = c.split(":")
        outs = outs.strip()
        outs = outs.split(" ")
        input[device] = outs
    f.close()
    return input

# 113037178808 too high
def rec_1(input, content, counter):
    if input == "out":
        return 1
    else:
        total = 0
        for node in content[input]:
            if node == "you":
                continue
            total += rec_1(node, content, counter)
        return total


def part_1(content):

    counter = 0
    for node in content["you"]:
        counter += rec_1(node, content, counter)

    print(counter)

def rec_2(input, content, path, paths):
    if input == "out":
        if "dac" in path or "fft" in path:
            print(path)
            return path
    else:
        for node in content[input]:
            if node in path:
                continue
            ind_path = copy.deepcopy(path)
            ind_path.append(node)
            f = rec_2(node, content, copy.deepcopy(ind_path), paths)
            paths.append(f)

def part_2(content):

    paths = []
    rec_2("svr", content, ["svr"], paths)
    counter = 0
    for el in paths:
        if el is None:
            continue
        print(el)

        if "dac" in el and "fft" in el:
            print("true")
            counter += 1


    return counter

def main():
    content = get_content("input_test.txt")
    test_1 = part_1(content)
    test_2 = part_2(content)

    content = get_content("input.txt")
    res_1 = part_1(content)
    res_2 = part_2(content)

    print("RESULT TEST 1:", test_1)
    print("RESULT 1:", res_1)
    print("RESULT TEST 2:", test_2)
    print("RESULT 2:", res_2)

if __name__ == '__main__':
    main()
