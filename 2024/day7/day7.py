from itertools import product

def level1():
    file = open("day7.txt", "r")


    content = file.readlines()
    final_sum = 0

    for line in content:
        calc = line.split(":")
        result = int(calc[0])
        numbers = calc[1].strip().split()
        numbers = [int(num) for num in numbers]

        print(result, numbers)

        chars = ['+', '*']
        combinations = list(product(chars, repeat=len(numbers) - 1))
        operators = [''.join(comb) for comb in combinations]

        calculated_result = 0
        already_counted = False
        for operator in operators:
            if operator[0] == "+":
                calculated_result = numbers[0] + numbers[1]
            if operator[0] == "*":
                calculated_result = numbers[0] * numbers[1]

            it = 1
            for i in range(2, len(numbers)):
                if operator[it] == "+":
                    calculated_result = calculated_result + numbers[i]
                if operator[it] == "*":
                    calculated_result = calculated_result * numbers[i]
                it += 1

            if result == calculated_result and not already_counted:
                already_counted = True
                final_sum += result

    print(final_sum)






def level2():
    file = open("day7.txt", "r")


    content = file.readlines()
    final_sum = 0

    for line in content:
        calc = line.split(":")
        result = int(calc[0])
        numbers = calc[1].strip().split()
        numbers = [int(num) for num in numbers]

        chars = ['+', '*', '|']
        combinations = list(product(chars, repeat=len(numbers) - 1))
        operators = [''.join(comb) for comb in combinations]

        calculated_result = 0
        already_counted = False
        for operator in operators:
            if operator[0] == "+":
                calculated_result = numbers[0] + numbers[1]
            if operator[0] == "*":
                calculated_result = numbers[0] * numbers[1]
            if operator[0] == "|":
                calculated_result = int(str(numbers[0]) + str(numbers[1]))

            it = 1
            for i in range(2, len(numbers)):
                if operator[it] == "+":
                    calculated_result = calculated_result + numbers[i]
                if operator[it] == "*":
                    calculated_result = calculated_result * numbers[i]
                if operator[it] == "|":
                    calculated_result = int(str(calculated_result) + str(numbers[i]))

                it += 1

            if result == calculated_result and not already_counted:
                already_counted = True
                final_sum += result

    print(final_sum)
if __name__ == '__main__':
    level1()
    level2()
