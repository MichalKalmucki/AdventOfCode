
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
        for i, seed in enumerate(seeds_cpy):
            if seed[0] >= source and seed[0] < source + amount - 1:
                if seed[1] > source + amount - 1:
                    if seed in seeds:
                        seeds.remove(seed)
                    seeds.append((seed[0] + destination - source, destination + amount - 1))
                    seeds_cpy[i] = (float('inf'), float('inf'))
                    seeds_cpy.append((source + amount, seed[1]))
                else:
                    seeds.append((seed[0] + destination - source, seed[1] + destination - source))
                    seeds_cpy[i] = (float('inf'), float('inf'))
                    if seed in seeds:
                        seeds.remove(seed)
            
            elif seed[1] > source and seed[1] < source + amount - 1:
                if seed in seeds:
                    seeds.remove(seed)
                seeds.append((destination, seed[1] + destination - source))
                seeds_cpy[i] = (float('inf'), float('inf'))
                seeds_cpy.append((seed[0], source - 1))

            elif seed[0] <= source and seed[1] > source + amount - 1:
                seeds_cpy[i] = (float('inf'), float('inf'))
                if seed in seeds:
                    seeds.remove(seed)
                if seed[0] < source:
                    seeds_cpy.append((seed[0], source))
                
                seeds.append((source + amount, seed[1]))
                seeds_cpy.append((destination, destination + amount - 1))

    for seed in seeds_cpy:
        if seed not in seeds and seed[0] != float('inf'):
            seeds.append(seed)              

    print(min(seeds, key=lambda x: x[0])[0])