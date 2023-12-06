with open('2023/6/input.txt', 'r') as file:
    lines = file.readlines()
    times = [int(num) for num in lines[0].split(':')[1].replace('\n', '').split()]
    records = [int(num) for num in lines[1].split(':')[1].replace('\n', '').split()]
    score = 1
    for i, time in enumerate(times):
        counter = 0
        for seconds in range(time):
            if seconds * (time - seconds) > records[i]:
                counter += 1
        score *= counter

    print(score)