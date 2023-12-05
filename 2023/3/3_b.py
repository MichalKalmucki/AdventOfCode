#function to return whole number under i,j and replace it with dots to not find it again later
def find_number(i, j, lines):
    number = []
    #check if under i,j there is a number
    j_temp = j
    if lines[i][j_temp] >= '0' and lines[i][j_temp] <= '9':
        #add left part of a number
        if j_temp - 1 >= 0 and lines[i][j_temp-1] >= '0' and lines[i][j_temp-1] <= '9':
            while j_temp - 1 >= 0 and lines[i][j_temp-1] >= '0' and lines[i][j_temp-1] <= '9':
                number.append(lines[i][j_temp-1])
                lines[i] = lines[i][:j_temp-1] + '.' + lines[i][j_temp:]
                j_temp -= 1
            number.reverse()

        #add middle of a number
        number.append(lines[i][j])
        lines[i] = lines[i][:j] + '.' + lines[i][j+1:]
        
        #add right part of a number
        j_temp = j
        if j_temp + 1 < len(lines[i]) and lines[i][j_temp+1] >= '0' and lines[i][j_temp+1] <= '9':
            while j_temp + 1 < len(lines[i]) and lines[i][j_temp+1] >= '0' and lines[i][j_temp+1] <= '9':
                number.append(lines[i][j_temp + 1])
                lines[i] = lines[i][:j_temp+1] + '.' + lines[i][j_temp+2:]
                j_temp += 1

    if len(number) == 0:
        return None, lines
    else:
        return number, lines

def find_nearby_numbers(i, j, lines):
    counter = 0
    numbers = []
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    for ny, nx in neighbors:
        number, lines = find_number(i + ny, j + nx, lines)
        if number is not None:
            numbers.append(int(''.join(number)))
            counter += 1
    return counter, numbers, lines

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        score = 0 
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == '*':
                    cnt, nearby, lines = find_nearby_numbers(i, j, lines)
                    if cnt == 2:
                        score += nearby[0] * nearby[1]
        print(score)

if __name__ == '__main__':
    main()