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
    content = get_content("input.txt")
    content = get_content("input_test.txt")
    print(part_1(content))
    print(part_2(content))

if __name__ == '__main__':
    main()
