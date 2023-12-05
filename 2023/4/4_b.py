import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    card_nums = np.zeros(len(lines), dtype=int) + 1
    for i, line in enumerate(lines):
        winning, selected = line[10:-1].split('|')
        winning = {int(num) for num in winning.split()}
        selected = [int(num) for num in selected.split()]
        card_score = 0
        winnings = np.sum([1 for num in selected if num in winning ], dtype=int)
        for idx in range(1, winnings + 1):
            card_nums[i + idx] += card_nums[i]
    print(np.sum(card_nums))