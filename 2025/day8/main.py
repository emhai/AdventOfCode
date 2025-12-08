import math
import itertools

def euclid_distance(value):
    p1, p2 = value[0], value[1]
    p1 = [int(i) for i in p1]
    p2 = [int(i) for i in p2]

    distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return distance

def get_content(file_name):
    f = open(file_name)
    content = f.read().splitlines()
    content = [i.strip().split(",") for i in content]
    f.close()
    return content

def part_1(content, amount):
    combinations = itertools.combinations(content, 2)
    combinations = list(combinations)
    combinations = sorted(combinations, key=euclid_distance)
    lights_in_circuit = []
    index_in_circuit = []

    circuits = {}
    counter = 0
    connections = 0
    for c in combinations:
        if len(lights_in_circuit) == len(content) or connections >= amount:
            break
        light_1, light_2 = c[0], c[1]
        if light_1 in lights_in_circuit and light_2 in lights_in_circuit:
            for key, val in circuits.items():
                if light_1 in val and light_2 not in val:
                    index_1 = lights_in_circuit.index(light_2)
                    index = index_in_circuit[index_1]
                    missing = circuits[index]
                    val.extend(missing)
                    for m in missing:
                        index2 = lights_in_circuit.index(m)
                        index_in_circuit[index2] = key
                    circuits.pop(index)
                    break
                elif light_2 in val and light_1 not in val:
                    index_1 = lights_in_circuit.index(light_1)
                    index = index_in_circuit[index_1]
                    missing = circuits[index]
                    val.extend(missing)
                    for m in missing:
                        index2 = lights_in_circuit.index(m)
                        index_in_circuit[index2] = key
                    circuits.pop(index)
                    break
                else:
                    continue

            connections += 1
        elif light_1 in lights_in_circuit or light_2 in lights_in_circuit:
            for key, val in circuits.items():
                if light_1 in val:
                    val.append(light_2)
                    lights_in_circuit.append(light_2)
                    index_in_circuit.append(key)
                elif light_2 in val:
                    val.append(light_1)
                    lights_in_circuit.append(light_1)
                    index_in_circuit.append(key)
            connections += 1
        else:
            lights_in_circuit.append(light_1)
            lights_in_circuit.append(light_2)
            index_in_circuit.append(counter)
            index_in_circuit.append(counter)
            circuits[counter] = [light_1, light_2]
            counter += 1
            connections += 1

    print("sorting")
    res = [k for k, v in sorted(circuits.items(), reverse=True, key=lambda item: len(item[1]))]
    mult = 1
    for i in range(3):
        mult *= len(circuits[res[i]])

    return mult

def part_2(content):
    combinations = itertools.combinations(content, 2)
    combinations = list(combinations)
    combinations = sorted(combinations, key=euclid_distance)
    lights_in_circuit = []
    index_in_circuit = []

    circuits = {}
    counter = 0
    connections = 0
    l1, l2 = 0,0
    for c in combinations:
        if len(lights_in_circuit) == len(content):
            break
        light_1, light_2 = c[0], c[1]
        l1, l2 = light_1, light_2
        if light_1 in lights_in_circuit and light_2 in lights_in_circuit:
            for key, val in circuits.items():
                if light_1 in val and light_2 not in val:
                    index_1 = lights_in_circuit.index(light_2)
                    index = index_in_circuit[index_1]
                    missing = circuits[index]
                    val.extend(missing)
                    for m in missing:
                        index2 = lights_in_circuit.index(m)
                        index_in_circuit[index2] = key
                    circuits.pop(index)
                    break
                elif light_2 in val and light_1 not in val:
                    index_1 = lights_in_circuit.index(light_1)
                    index = index_in_circuit[index_1]
                    missing = circuits[index]
                    val.extend(missing)
                    for m in missing:
                        index2 = lights_in_circuit.index(m)
                        index_in_circuit[index2] = key
                    circuits.pop(index)
                    break
                else:
                    continue

            connections += 1
        elif light_1 in lights_in_circuit or light_2 in lights_in_circuit:
            for key, val in circuits.items():
                if light_1 in val:
                    val.append(light_2)
                    lights_in_circuit.append(light_2)
                    index_in_circuit.append(key)
                elif light_2 in val:
                    val.append(light_1)
                    lights_in_circuit.append(light_1)
                    index_in_circuit.append(key)
            connections += 1
        else:
            lights_in_circuit.append(light_1)
            lights_in_circuit.append(light_2)
            index_in_circuit.append(counter)
            index_in_circuit.append(counter)
            circuits[counter] = [light_1, light_2]
            counter += 1
            connections += 1

    mult = int(l1[0]) * int(l2[0])
    return mult

def main():
    content = get_content("input_test.txt")
    test_1 = part_1(content, 10)
    test_2 = part_2(content)

    content = get_content("input.txt")
    res_1 = part_1(content,  1000)
    res_2 = part_2(content)

    print("RESULT TEST 1:", test_1)
    print("RESULT 1:", res_1)
    print("RESULT TEST 2:", test_2)
    print("RESULT 2:", res_2)

if __name__ == '__main__':
    main()
