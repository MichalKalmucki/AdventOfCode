
#Create hand score by multiplying each hand by 10 to the power of 10 minus 2 times the index of the card in the hand
#Add 10^12 times the score of the hand type
#This way most important factor is always hand type, and then card in fist place in hand and so on...
def hand_score(hand, card_scores):
    score = 0
    counts = {}
    for i, card in enumerate(hand):
        score += 10**(10-i*2) * card_scores[card]
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    counts = [count for count in sorted(counts.values(), reverse=True)[:2]]
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
        card_scores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

        all_hands = []
        for line in lines:
            hand, bid = line.replace('\n', '').split()
            all_hands.append((hand_score(hand, card_scores), int(bid)))

        all_hands = [(i+1)*bid for i, (_,bid) in enumerate(sorted(all_hands, key=lambda x: x[0]))]
        
        print(sum(all_hands))

if __name__ == '__main__':
    main()