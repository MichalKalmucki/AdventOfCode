from bisect import bisect_left, bisect_right

with open('2023/5/input.txt', 'r') as f:
    lines = f.readlines()
    seeds_line = [int(seed) for seed in lines[0][7:].split()]
    seeds = []
    for i in range(len(seeds_line)//2):
        start, quantity = seeds_line[i*2], seeds_line[i*2+1]
        seeds.append((start, start + quantity - 1))
    print(seeds)
    seeds_cpy = seeds.copy()
    for line in lines[3:]:
        if line[0].isspace():
            for seed in seeds_cpy:
                if seed not in seeds:
                    seeds.append(seed)
            seeds_cpy = seeds.copy()
            print(seeds)
        if line[0] < '0' or line[0] > '9':
            continue
        destination, source, amount = [int(num) for num in line.replace('\n', '').split()]
        start_index = bisect_left(seeds, source, key=lambda x: x[0])
        end_index = bisect_right(seeds, source + amount - 1, key=lambda x: x[1])
        print(start_index, end_index, source, amount, destination)  
        # print(f'seeds_cpy = {seeds_cpy}')
        for i, seed in enumerate(seeds):
            if seed[0] > source and seed[0] < source + amount - 1:
                if seed[1] > source + amount - 1:
                    if seed in seeds:
                        seeds.remove(seed)
                    seeds.append((source + amount, seed[1]))
                    if seed in seeds_cpy:
                        seeds_cpy.remove(seed)
                    seeds_cpy.append((seed[0] + destination - source, destination + amount - 1))
                else:
                    if seed in seeds:
                        seeds.remove(seed)
                    seeds_cpy.append((seed[0] + destination - source, seed[1] + destination - source))
                    if seed in seeds_cpy:
                        seeds_cpy.remove(seed)
                    print(f'seeds: {(seed[0] + destination - source, seed[1] + destination - source)}')
                    print(f'seed = {seed}')
                    print(seeds)
                    print(seeds_cpy)
                    
            elif seed[1] > source and seed[1] < source + amount - 1:
                seeds[i] = (seed[0], source - 1)
                if seed in seeds_cpy:
                    seeds_cpy.remove(seed)
                seeds_cpy.append((destination, seed[1] + destination - source))

            elif seed[0] <= source and seed[1] > source + amount - 1:
                if seed in seeds_cpy:
                    seeds_cpy.remove(seed)
                if seed in seeds:
                    seeds.remove(seed)
                if seed[0] < source:
                    seeds.append((seed[0], source))
                    seeds_cpy.append((seed[0], source))
                
                seeds.append((source + amount, seed[1]))
                
                seeds_cpy.append((destination, destination + amount - 1))

    for seed in seeds_cpy:
        if seed not in seeds:
            seeds.append(seed)              

    print(sorted(seeds, key=lambda x: x[0]))