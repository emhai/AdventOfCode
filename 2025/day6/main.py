import os

def get_content(file_name):
    f = open(file_name)
    content = f.read()
    f.close()
    return content

def part_1(content):
    content = content.splitlines()
    content = [i.strip() for i in content]
    content = [i.split() for i in content]

    no_digits = len(content)
    no_calculations = len(content[0])
    overall_result = 0
    for i in range(no_calculations):

        math_op = content[-1][i]
        result = 0 if math_op == "+" else 1
        for j in range(no_digits - 1):
            digit = int(content[j][i])
            if math_op == "+":
                result += digit
            else:
                result *= digit

        overall_result += result
    return overall_result

def part_2(content):

    content = content.splitlines()
    no_digits = len(content)
    overall_result = 0
    content = [list(i) for i in content]
    ids = []
    for i in range(len(content[-1])):
        if content[-1][i] == "+" or content[-1][i] == "*":
            ids.append(i)

    last_index = 0
    for row in content:
        if len(row) > last_index:
            last_index = len(row)
    ids.append(last_index)
    for i in range(1, len(ids)):
        id1 = ids[i - 1]
        id2 = ids[i]
        math_op = ""
        numbers = []
        for j in range(id2 - 1, id1 - 1, -1):
            number = ""
            for row in range(no_digits):
                if j >= len(content[row]):
                    continue
                new_char = content[row][j]
                if new_char.isdigit():
                    number += new_char
                elif new_char == "*" or new_char == "+":
                    math_op = new_char
                else:
                    continue

            if len(number) > 0:
                numbers.append(number)

        print("final", numbers, math_op)
        if math_op == "*":
            result = 1
        else:
            result = 0
        for num in numbers:
            print(num)
            if math_op == "*":
                result *= int(num)
            else:
                result += int(num)
        print(result)
        overall_result += result



    return overall_result
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
