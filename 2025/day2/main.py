import os

def get_content(file_name):
    f = open(file_name)
    content = f.read().split(',')
    f.close()
    return content

def part_1(content):

    counter = 0
    for range_val in content:
        first_num, second_num = range_val.split('-')

        for num in range(int(first_num), int(second_num) + 1):
            no_digit = int(len(str(num)) / 2)
            p1, p2 = str(num)[:no_digit], str(num)[no_digit:]
            if p1 == p2:
                counter += num

    return counter

def part_2(content):

    counter = 0
    for range_val in content:
        first_num, second_num = range_val.split('-')
        for num in range(int(first_num), int(second_num) + 1):
            num = str(num)
            no_digit = len(str(num))
            match = False
            for n in range(1, no_digit):
                if match:
                    continue

                test = [num[i:i + n] for i in range(0, len(num), n)]
                prev_item = None
                every_item = True
                for item in test:
                    if prev_item is None:
                        prev_item = item
                        continue

                    if prev_item != item:
                        every_item = False

                if every_item:
                    match = True
                if match:
                    print(num)
                    counter += int(num)

    return counter


def main():
    content = get_content("input.txt")
    # content = get_content("input_test.txt")
    print(part_1(content))
    print(part_2(content))

if __name__ == '__main__':
    main()
