import numpy as np

with open('2023/5/input.txt', 'r') as f:
    lines = f.readlines()
    seeds = np.sort(np.array([int(seed) for seed in lines[0][7:].split()], dtype=np.int64))
    seeds_cpy = seeds.copy()
    for line in lines[1:]:
        if line[0].isspace():
            seeds_cpy = np.sort(seeds_cpy)
            seeds = seeds_cpy.copy()
        if line[0] < '0' or line[0] > '9':
            continue
        
        destination, source, ammount = [int(num) for num in line.replace('\n', '').split()]
        start_index = np.searchsorted(seeds, source, side='left')
        end_index = np.searchsorted(seeds, source + ammount - 1, side='right')
        if len(seeds[start_index:end_index]) > 0:
            seeds_cpy[start_index:end_index] += destination - source

    print(np.min(seeds_cpy))