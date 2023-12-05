with open('input.txt') as f:
    lines = f.readlines()
    score = 0 
    for line in lines:
        winning, selected = line.split(':')[1][1:-1].split('|')
        winning = {int(num) for num in winning.split()}
        selected = [int(num) for num in selected.split()]
        card_score = 0
        for num in selected:
            if num in winning:
                if card_score == 0:
                    card_score += 1
                else:
                    card_score *= 2
        score += card_score
    print(score)