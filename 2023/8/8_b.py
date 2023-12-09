from itertools import cycle
from math import lcm

def create_node_map():
    with open('2023/8/input.txt', 'r') as file:
        lines = file.readlines()
        instrucions = lines[0].rstrip('\n')
        node_map = {}
        starting_nodes = []
        for line in lines[2:]:
            node, neighbors = line.rstrip('\n').split(' = ')
            node_map[node] = neighbors[1:-1].split(', ')
            if node[-1] == 'A':
                starting_nodes.append(node)
    return node_map, instrucions, starting_nodes

def main():
    node_map, instructions, current_nodes = create_node_map()
    counters = []
    for node_id, node in enumerate(current_nodes):
        for i, lr in enumerate(cycle(instructions), 1):
            if lr == 'L':
                current_nodes[node_id] = node_map[current_nodes[node_id]][0]
            else:
                current_nodes[node_id] = node_map[current_nodes[node_id]][1]

            if current_nodes[node_id][-1] == 'Z':
                counters.append(i)
                break
    
    #this works only bercause node ending with z is at the end of the cycle for each starting node
    print(lcm(*counters))

if __name__ == '__main__':
    main()