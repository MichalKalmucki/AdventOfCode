import re

with open('input.txt') as f:
    lines = f.readlines()
    cubes = {'red':12, 'green':13, 'blue':14}
    output = 0
    for line in lines:
        id, result = line.split(':')
        id = id.strip('Game ')
        possible = True
        pattern = r'[;,]'
        result = re.split(pattern, result[:-1])
        for res in result:
            num, color = res.split()
            if cubes[color] < int(num):
                possible = False
        if possible:
            output += int(id)
    print(output)