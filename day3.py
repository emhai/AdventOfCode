def level1():
    file = open("day3.txt", "r")
    data = []
    first_line = file.readline()
    length = len(first_line)
    data.append(["."] * (length + 2))
    file.seek(0)
    for line in file:
        row = ["."]
        for x in line:
            if x != "\n":
                row.append(x)
        row.append(".")
        data.append(row)
    data.append(["."] * (length + 2))

    total_number = 0
    i = 0
    while i < len(data):
        row = data[i]
        j = 0
        while j < len(row):
            if not data[i][j].isnumeric():
                j += 1
                continue

            index = 0
            num = ""
            while data[i][j + index].isnumeric():
                num += data[i][j + index]
                index += 1

            engine_number = False
            for check_i in range(j - 1, j + index + 1):
                for check_j in range(i - 1, i + 2, 1):
                    symbol = data[check_j][check_i]
                    # print(check_i, check_j, symbol)
                    if symbol != "." and not symbol.isnumeric():
                        engine_number = True

            if engine_number:
                print(num)
                total_number += int(num)
            j += index + 1
        i += 1

    print(total_number)


def level2():
    file = open("day3.txt", "r")
    data = []
    first_line = file.readline()
    length = len(first_line)
    data.append(["."] * (length + 2))
    file.seek(0)
    for line in file:
        row = ["."]
        for x in line:
            if x != "\n":
                row.append(x)
        row.append(".")
        data.append(row)
    data.append(["."] * (length + 2))

    total_sum = 0
    i = 0
    while i < len(data):
        row = data[i]
        j = 0
        while j < len(row):
            if data[i][j] == "*":
                nums = []

                for star_i in range(i-1, i+2):
                    for star_j in range(j-1, j+2):
                        offset = 0
                        if not data[star_i][star_j].isnumeric():
                            continue

                        while data[star_i][star_j - offset].isnumeric():
                            print("finding start", star_i, star_j - offset, data[star_i][star_j - offset])
                            offset += 1
                        offset = star_j - offset + 1
                        print("offset", offset)
                        num = ""
                        while data[star_i][offset].isnumeric():
                            print("finding end", star_i, offset, data[star_i][offset])
                            num += data[star_i][offset]
                            offset += 1
                        if num not in nums:
                            nums.append(num)
                print(nums)
                if len(nums) == 2:
                    total_sum += int(nums[0]) * int(nums[1])
            j += 1
        i += 1

        print(total_sum)









if __name__ == '__main__':
    # level1()
    level2()
