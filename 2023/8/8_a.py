from itertools import cycle

def create_node_map():
    with open('2023/8/input.txt', 'r') as file:
        lines = file.readlines()
        instrucions = lines[0].rstrip('\n')
        node_map = {}
        for line in lines[2:]:
            node, neighbors = line.rstrip('\n').split(' = ')
            node_map[node] = neighbors[1:-1].split(', ')
    return node_map, instrucions

def main():
    node_map, instructions = create_node_map()
    current = 'AAA'
    for i, lr in enumerate(cycle(instructions), 1):
        if lr == 'L':
            current = node_map[current][0]
        else:
            current = node_map[current][1]

        if current == 'ZZZ':
            break
    print(i)


if __name__ == '__main__':
    main()