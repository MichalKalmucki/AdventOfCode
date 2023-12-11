with open('2023/10/input.txt', 'r') as file:
    lines = file.readlines()

def get_starting_node(m, n):
    if m > 0 and lines[m - 1][n] in ('|', '7', 'F'):
        direction = 'd'
        m -= 1
    elif m < len(lines) - 1 and lines[m + 1][n] in ('|', 'J', 'L'):
        direction = 'u'
        m += 1
    elif n > 0 and lines[m][n - 1] in ('-', 'L', 'F'):
        direction = 'r'
        n -= 1
    elif n < len(lines[0]) - 1 and lines[m][n + 1] in ('-', 'J', '7'):
        direction = 'l'
        n += 1
    return m, n, direction

#Create set of moves and follow it till you reach starting point back, then return the length of the path divided by 2
def main():

    moves = {
        ('J', 'l'): (-1, 0, 'd'),
        ('J', 'u'): (0, -1, 'r'),
        ('L', 'r'): (-1, 0, 'd'),
        ('L', 'u'): (0, 1, 'l'),
        ('7', 'l'): (1, 0, 'u'),
        ('7', 'd'): (0, -1, 'r'),
        ('F', 'r'): (1, 0, 'u'),
        ('F', 'd'): (0, 1, 'l'),
        ('|', 'u'): (1, 0, 'u'),
        ('|', 'd'): (-1, 0, 'd'),
        ('-', 'l'): (0, 1, 'l'),
        ('-', 'r'): (0, -1, 'r'),
    }

    m, start_line = [(m, line) for m, line in enumerate(lines) if 'S' in line][0]
    n = start_line.find('S')
    m, n, direction = get_starting_node(m, n)

    node = lines[m][n]
    path = []
    while node != 'S':
        path.append(node)
        i, j, direction = moves[(node, direction)]
        m, n = m + i, n + j
        node = lines[m][n]
    print(len(path)//2 + 1)

if __name__ == '__main__':
    main()