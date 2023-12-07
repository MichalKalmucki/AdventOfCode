
#Same idea as for task 1 but, include additional logic for jokers
def hand_score(hand, card_scores):
    score = 0
    counts = {}
    for i, card in enumerate(hand):
        score += 10**(10-i*2) * card_scores[card]
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    Joker_count = counts.pop('J', 0)

    counts = [count for count in sorted(counts.values(), reverse=True)[:2]]
    if len(counts) > 0:
        counts[0] += Joker_count
    else:
        counts.append(Joker_count)
    #Check hand type
    if counts[0] == 5:
        score += 10**12*9
    elif counts[0] == 4:
        score += 10**12*8
    elif counts[0] == 3 and counts[1] == 2:
        score += 10**12*7
    elif counts[0] == 3:
        score += 10**12*6
    elif counts[0] == 2 and counts[1] == 2:
        score += 10**12*5
    elif counts[0] == 2:
        score += 10**12*4

    return score

def main():
    with open('2023/7/input.txt', 'r') as f:
        lines = f.readlines()
        card_scores = {'J':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8':8, '9':9, 'T':10, 'Q':11, 'K':12, 'A':13}

        all_hands = []
        for line in lines:
            hand, bid = line.replace('\n', '').split()
            all_hands.append((hand_score(hand, card_scores), int(bid)))

        all_hands = [(i+1)*bid for i, (_,bid) in enumerate(sorted(all_hands, key=lambda x: x[0]))]
        
        print(sum(all_hands))

if __name__ == '__main__':
    main()