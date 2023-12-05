

with open('input.txt') as f:
    lines = f.readlines()
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    score = 0 
    for i, line in enumerate(lines):
        current = []
        is_nearby = False
        for j, char in enumerate(line):
            if char >= '0'  and char <= '9':
                current.append(char)
                for n in neighbors:
                    if i + n[0] >= 0 and i + n[0] < len(lines) and j + n[1] >= 0 and j + n[1] < len(line):
                        if not lines[i + n[0]][j + n[1]].isdigit() and lines[i + n[0]][j + n[1]] != '.' and lines[i + n[0]][j + n[1]] != '\n':
                            is_nearby = True
                
            else:
                if len(current) > 0:
                    if is_nearby:
                        score += int(''.join([x for x in current]))
                    is_nearby = False
                    current = []
    print(score)