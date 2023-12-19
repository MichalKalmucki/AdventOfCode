import sys
sys.setrecursionlimit(15000)

# was oop overkill? maybe, but it is a nice way to avoid global variables
class BeamSolver():
    def __init__(self):
        self.lines = [line.rstrip() for line in open('2023/16/input.txt', 'r')]
        self.iluminated = [[False for _ in range(len(self.lines[0]))] for _ in range(len(self.lines))]
        self.visited = set()

    
    def beam_traverse(self, prev_x, prev_y, x, y):
        if x < 0 or y < 0 or x >= len(self.lines[0]) or y >= len(self.lines) or (prev_x, prev_y, x, y) in self.visited:
            return
        next_x, next_y = x, y

        self.iluminated[y][x] = True
        self.visited.add((prev_x, prev_y, x, y))

        #moves that continue previous movement
        if self.lines[y][x] == '.': 
            next_x, next_y = 2 * x - prev_x, 2 * y - prev_y
        
        elif self.lines[y][x] == '|':
            if prev_x == x: 
                next_y = 2 * y - prev_y
            else:
                # splitting
                self.beam_traverse(x, y, x, y + 1)
                next_y -= 1
        
        elif self.lines[y][x] == '-': 
            if prev_y == y:
                next_x = 2 * x - prev_x
            else:
                # splitting
                self.beam_traverse(x, y, x + 1, y)
                next_x -= 1

        #90 degree turns
        elif self.lines[y][x] == '/' and  prev_y == y:
            next_y -= (x - prev_x)
        
        elif self.lines[y][x] == '/' and prev_x == x:
            next_x -= (y - prev_y)
        
        elif self.lines[y][x] == '\\' and prev_y == y:
            next_y += (x - prev_x)

        elif self.lines[y][x] == '\\' and prev_x == x:
            next_x += (y - prev_y)

        self.beam_traverse(x, y, next_x, next_y)
    
    def find_first(self):
        self.visited = set()
        self.iluminated = [[False for _ in range(len(self.lines[0]))] for _ in range(len(self.lines))]
        self.beam_traverse(-1, 0, 0, 0)
        print(sum(sum(row) for row in self.iluminated))

    def find_best(self):
        best_score = 0 
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                if i == 0 or j == 0 or i == len(self.lines) - 1 or j == len(self.lines[0]) - 1:
                    self.iluminated = [[False for _ in range(len(self.lines[0]))] for _ in range(len(self.lines))]
                    self.visited = set()
                    if i == 0:
                        self.beam_traverse(j, i - 1, j, i)
                    elif j == 0:
                        self.beam_traverse(j - 1, i, j, i)
                    elif i + 1 == len(self.lines):
                        self.beam_traverse(j, i + 1, j, i)
                    elif j + 1 == len(self.lines[0]):
                        self.beam_traverse(j + 1, i, j, i)

                    score = sum(sum(row) for row in self.iluminated)
                    best_score = max(best_score, score)
        print(best_score)

def main():
    solver = BeamSolver()
    solver.find_first()
    solver.find_best()


if __name__ == '__main__':
    main()