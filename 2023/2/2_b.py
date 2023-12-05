import re
import numpy as np

with open('2023/2/input.txt') as f:
    lines = f.readlines()
    output = 0
    for line in lines:
        cubes = {'red':0, 'green':0, 'blue':0}
        id, result = line.split(':')
        id = id.strip('Game ')
        pattern = r'[;,]'
        result = re.split(pattern, result)
        for res in result:
            num, color = res.split()
            if cubes[color] < int(num):
                cubes[color] = int(num)
        
        output += np.prod([cubes[color] for color in cubes])
    print(output)