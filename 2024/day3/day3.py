import re


def level1():
    file = open("day3.txt", "r")

    content = file.read()
    x = re.findall("mul\(\d{1,3},\d{1,3}\)", content)
    sum = 0
    for mul in x:
        calc = str(mul).split(",")
        number1 = calc[0][len("mul("):]
        number2 = calc[1][:-1]
        sum += int(number1) * int(number2)
    print(sum)




def level2():
    file = open("day3.txt", "r")

    content = file.read()
    x = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", content)
    enable = True
    sum = 0

    for mul in x:
        if mul == "do()":
            enable = True
        elif mul == "don't()":
            enable = False
        else:
            if enable:
                calc = str(mul).split(",")
                number1 = calc[0][len("mul("):]
                number2 = calc[1][:-1]
                sum += int(number1) * int(number2)

    print(sum)



if __name__ == '__main__':
    level1()
    level2()
