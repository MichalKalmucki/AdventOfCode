import numpy as np

def do_cycle(rocks_map):
    for _ in range(4):
        n = rocks_map.shape[0]
        for row in rocks_map.T:
            rock_count = 0
            starting_point = 0
            for i, point in enumerate(row):
                if point == 'O':
                    rock_count += 1
                    row[i] = '.'
                elif point == '#':
                    row[starting_point:starting_point+rock_count] = 'O'
                    starting_point = i + 1
                    rock_count = 0
            row[starting_point:starting_point+rock_count] = 'O'
        rocks_map = np.rot90(rocks_map, 3)
    return rocks_map

def do_n_cycles(rocks_map, n):
    visited = {}
    prev, i = None, 0
    while i < n:
        rocks_map = do_cycle(rocks_map)
        if (prev, rocks_map.tobytes()) in visited:
            cycle_len = i - visited[(prev, rocks_map.tobytes())]
            i = n - (n - i) % cycle_len
        else:
            visited[(prev, rocks_map.tobytes())] = i

        prev = rocks_map.tobytes()
        i += 1

    return rocks_map

def main():
    rocks_map = np.array([list(a.rstrip()) for a in open('2023/14/input.txt')])
    score = 0
    rocks_map = do_n_cycles(rocks_map, 1000000000)
    n = rocks_map.shape[0]
    multiply_by = np.tile(np.arange(n, 0, -1), (n, 1)).T
    score = np.sum(np.where(rocks_map == 'O', multiply_by, 0))
    print(score)

if __name__ == '__main__':
    main()