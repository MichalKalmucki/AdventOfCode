import math


with open('2023/6/input.txt', 'r') as file:
    lines = file.readlines()
    time = int(lines[0].split(':')[1].replace('\n', '').replace(' ', ''))
    record = int(lines[1].split(':')[1].replace('\n', '').replace(' ', ''))
    delta = time**2 - 4 * record
    x1 = (-time + math.sqrt(delta)) / 2
    x2 = (-time - math.sqrt(delta)) / 2

    print(math.floor(abs(x1 - x2)))