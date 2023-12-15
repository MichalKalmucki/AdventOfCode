import numpy as np

rocks_map = np.array([list(a.rstrip()) for a in open('2023/14/input.txt')])

score = 0
n = rocks_map.shape[0]

for row in rocks_map.T:
    rock_count = 0
    starting_point = 0
    for i, point in enumerate(row):
        if point == 'O':
            rock_count += 1
        elif point == '#':
            score += sum([a for a in  range(n + 1)[::-1][starting_point:starting_point+rock_count]])
            starting_point = i + 1
            rock_count = 0
    score += sum([a for a in  range(n + 1)[::-1][starting_point:starting_point+rock_count]])
print(score)
