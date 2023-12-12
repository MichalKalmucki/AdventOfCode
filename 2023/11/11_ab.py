import numpy as np

def get_lines():
    with open('2023/11/input.txt', 'r') as f:
        lines = np.array([[8 if char == '#' else 1 for char in line.strip()] for line in f.readlines()])
        indices = np.where(lines == 8)
        indices = np.column_stack(indices)
        return lines, indices

def task(expand_by):
    lines, indices = get_lines()
    expanded_rows = np.where(np.sum(lines, axis=1) == len(lines[0]))[0]
    expanded_cols = np.where(np.sum(lines, axis=0) == len(lines))[0]
    score = 0
    for i, id1 in enumerate(indices[:-1]):
        for id2 in indices[i+1:]:
            score += np.abs(id1[0] - id2[0]) + np.abs(id1[1] - id2[1])
            score += expand_by*(np.searchsorted(expanded_rows, max(id1[0], id2[0])) - np.searchsorted(expanded_rows, min(id1[0], id2[0])))
            score += expand_by*(np.searchsorted(expanded_cols, max(id1[1], id2[1])) - np.searchsorted(expanded_cols, min(id1[1], id2[1])))
    print(score)

def main():
    task(1)
    task(999_999)

if __name__ == '__main__':
    main()