import numpy as np

def task(task_num):
    with open('2023/9/input.txt', 'r') as file:
        lines = file.readlines()
        result = np.array([])
        for line in lines:
            sequence = np.array([int(num) for num in line.rstrip('\n').split()])[::task_num]
            seq1 = sequence[:-1]
            seq2 = sequence[1:]
            seqs = [sequence]
            while np.any(seq2 - seq1 != 0):
                seq = seq2 - seq1
                seqs.append(seq)
                seq1 = seq[:-1]
                seq2 = seq[1:]
            predicted = 0
            seqs = seqs[::-1]
            for i, seq in enumerate(seqs[:-1]):
                predicted = seqs[i + 1][-1] + seqs[i][-1]
                seqs[i + 1] = np.append(seqs[i + 1], predicted)
            result = np.append(result, seqs[-1][-1])

        return np.sum(result, dtype=np.int64)

def main():
    #task1
    print(task(1))
    #task2
    print(task(-1))

if __name__ == '__main__':
    main()