input = open("2023/15/input.txt", "r").read().split(',')
scores = []
for word in input:
    score = 0
    for char in word:
        score = (ord(char) + score) * 17
        score %= 256
    scores.append(score)
print(sum(scores))