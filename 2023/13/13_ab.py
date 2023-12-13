import numpy as np

#Use numpy to slice matrix in possible mirror positions and compare them
def find_mirror(matrix, num_diff):
    for i in range(len(matrix[0])):
        low_bound = max(0, 2 *(i+1)-len(matrix[0]))
        if np.sum(matrix[:,low_bound:i + 1] != matrix[:,i + 1:2*i - low_bound + 2][::, ::-1] ) == num_diff and matrix[:,low_bound:i + 1].shape[1] > 0:
            return i
            
def task(inputs, task_num):
    score = 0
    for matrix in inputs:
        matrix = np.array(matrix)
        mirror_position = find_mirror(matrix, task_num)
        if mirror_position is not None:
            score += mirror_position + 1
        else:
            mirror_position = find_mirror(matrix.T, task_num)
            score += (mirror_position + 1) * 100
    print(f'Score: {score}')

def main():
    lines = [list(line.rstrip()) for line in open('2023/13/input.txt')]
    inputs = []
    current = []
    for line in lines:
        if line == []:
            inputs.append(current)
            current = []
            continue
        current.append(line)
    inputs.append(current)

    task(inputs, 0)
    task(inputs, 1)

if __name__ == '__main__':
    main()