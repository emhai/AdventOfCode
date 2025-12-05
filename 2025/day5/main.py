
def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    f.close()
    return content

def part_1(content):

    fresh_low = []
    fresh_high = []
    counter = 0
    for line in content:
        if len(line) == 0:
            continue

        if "-" in line:
            low, up = line.split("-")
            fresh_low.append(int(low))
            fresh_high.append(int(up))
        else:
            for i in range(len(fresh_low)):
                if fresh_low[i] < int(line) <= fresh_high[i]:
                    counter += 1
                    break

    return counter


def part_2(content):

    fresh_low = []
    fresh_high = []
    for line in content:
        if "-" not in line:
            continue
        low, high = line.split("-")
        low, high = int(low), int(high)
        fresh_low.append(low)
        fresh_high.append(high)

    lows, highs = (list(t) for t in zip(*sorted(zip(fresh_low, fresh_high))))
    print(lows)
    print(highs)
    done = False
    freshs = []
    i = 0
    while not done:
        if i >= len(lows):
            done = True
            continue

        high = highs[i]
        low = lows[i]
        j = i
        while True:
            j += 1
            if j >= len(lows):
                done = True
                j = len(lows) - 1
                break

            if high < lows[j]:
                j -= 1
                break

            if high < highs[j]:
                high = max(high, highs[j])



        freshs.append((low, max(high, highs[j])))
        i = j + 1

    counter = 0
    print(freshs)
    for fresh_range in freshs:
        amount = fresh_range[1] - fresh_range[0] + 1
        counter += amount

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
