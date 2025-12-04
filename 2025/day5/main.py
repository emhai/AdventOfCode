import os

def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    f.close()
    return content

def part_1(content):

    return

def part_2(content):

    return

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
