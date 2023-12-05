
with open('input.txt', 'r') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for number in numbers:
            line = line.replace(number, number + str(numbers.index(number)) + number)
        line_digits = ''.join(filter(str.isdigit, line))
        total += int(line_digits[0] + line_digits[-1])
    print(total)