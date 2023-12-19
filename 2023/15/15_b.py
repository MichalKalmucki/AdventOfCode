input = open("2023/15/input.txt", "r").read().split(',')
boxes = [dict() for _ in range(256)]

def HASH (word):
    score = 0
    for char in word:
        score = (ord(char) + score) * 17
        score %= 256
    return score

for word in input:
    if '=' in word:
        lens, size = word.split('=')
        boxes[HASH(lens)][lens] = int(size)
    if '-' in word:
        lens = word.strip('-')
        boxes[HASH(lens)].pop(lens, 0)

score = 0
print(sum(i*j*f for i,b in enumerate(boxes, 1)
                for j,f in enumerate(b.values(), 1)))