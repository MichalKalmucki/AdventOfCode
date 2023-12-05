import re
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    output = 0
    for line in lines:
        cubes = {'red':0, 'green':0, 'blue':0}
        id, result = line.split(':')
        id = id.strip('Game ')
        pattern = r'[;,]'
        result = re.split(pattern, result[:-1])
        for res in result:
            num, color = res.split()
            if cubes[color] < int(num):
                cubes[color] = int(num)
        
        output += np.prod([cubes[color] for color in cubes])
    print(output)