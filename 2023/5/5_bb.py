from bisect import bisect_left, bisect_right

with open('2023/5/input.txt', 'r') as f:
    lines = f.readlines()
    seeds_line = [int(seed) for seed in lines[0][7:].split()]
    seeds = []
    for i in range(len(seeds_line)//2):
        start, quantity = seeds_line[i*2], seeds_line[i*2+1]
        seeds.append((start, start + quantity - 1))
    seeds_cpy = seeds.copy()
    for line in lines[3:]:
        if line[0].isspace():
            for seed in seeds_cpy:
                if seed not in seeds and seed[0] != float('inf'):
                    seeds.append(seed)
            seeds_cpy = seeds.copy()

        if line[0] < '0' or line[0] > '9':
            continue
        destination, source, amount = [int(num) for num in line.replace('\n', '').split()]
        # start_index = bisect_left(seeds, source, key=lambda x: x[0])
        # end_index = bisect_right(seeds, source + amount - 1, key=lambda x: x[1])
        for i, seed in enumerate(seeds_cpy):
            if seed[0] >= source and seed[0] < source + amount - 1:
                if seed[1] > source + amount - 1:
                    if seed in seeds:
                        seeds.remove(seed)
                    seeds.append((seed[0] + destination - source, destination + amount - 1))
                    seeds_cpy[i] = (float('inf'), float('inf'))
                    seeds_cpy.append((source + amount, seed[1]))
                    # if (seed[0] + destination - source, destination + amount - 1) == (7971591, 30062974) or (source + amount, seed[1]) == (7971591, 30062974):
                    #     print(f'1 {seed}')
                    #     exit()
                else:
                    seeds.append((seed[0] + destination - source, seed[1] + destination - source))
                    seeds_cpy[i] = (float('inf'), float('inf'))
                    if seed in seeds:
                        seeds.remove(seed)
                    print(f'destination {destination}, source {source}, amount {amount}')
                    print(f'seed {seed}')
                    print(f'normal {(seed[0] + destination - source, seed[1] + destination - source)}')
                    if (seed[0] + destination - source, seed[1] + destination - source) == (7971591, 30062974):
                        print(f'2 {seed}')
                        exit()
            
            elif seed[1] > source and seed[1] < source + amount - 1:
                if seed in seeds:
                    seeds.remove(seed)
                seeds.append((destination, seed[1] + destination - source))
                seeds_cpy[i] = (float('inf'), float('inf'))
                seeds_cpy.append((seed[0], source - 1))
                # print(f'destination {destination}, source {source}, amount {amount}')
                # print(f'seed {seed}')
                # print(f'normal {destination, seed[1] + destination - source})')
                # print(f'cpy {seed[0], source - 1})')

                # if (destination, seed[1] + destination - source) == (7971591, 30062974) or (seed[0], source - 1) == (7971591, 30062974):
                #     print(f'3 {seed}', destination, source, amount)
                #     exit()

            elif seed[0] <= source and seed[1] > source + amount - 1:
                seeds_cpy[i] = (float('inf'), float('inf'))
                if seed in seeds:
                    seeds.remove(seed)
                if seed[0] < source:
                    seeds_cpy.append((seed[0], source))
                
                seeds.append((source + amount, seed[1]))
                seeds_cpy.append((destination, destination + amount - 1))
                # if (seed[0], source) == (7971591, 30062974) or (source + amount, seed[1]) == (7971591, 30062974):
                #     print(f'4 {seed}')
                #     exit()

    for seed in seeds_cpy:
        if seed not in seeds and seed[0] != float('inf'):
            seeds.append(seed)              

    print(sorted(seeds, key=lambda x: x[0]))