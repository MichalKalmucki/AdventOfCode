import cv2
import numpy as np
import matplotlib.pyplot as plt

#I thought it will be fun to solve this problem with OpenCV since we practiced using this library during computer vision classes.

with open('2023/10/input.txt', 'r') as file:
    lines = file.readlines()

def get_starting_node(m, n):
    i, j = 0, 0
    if m > 0 and lines[m - 1][n] in ('|', '7', 'F'):
        direction = 'd'
        i -= 1
    elif m < len(lines) - 1 and lines[m + 1][n] in ('|', 'J', 'L'):
        direction = 'u'
        i += 1
    elif n > 0 and lines[m][n - 1] in ('-', 'L', 'F'):
        direction = 'r'
        j -= 1
    elif n < len(lines[0]) - 1 and lines[m][n + 1] in ('-', 'J', '7'):
        direction = 'l'
        j += 1
    return i, j, direction

#Use approach from first task to create path, draw it as an binary image, use opencv findContours function to find pixels inside loop
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

    #image needs to be 2 times bigger than maze to account for possibility of "squeezing" between pipes
    img_bin = np.zeros((len(lines) * 2, len(lines[0][:-1]) * 2), np.uint8)
    m, start_line = [(m, line) for m, line in enumerate(lines) if 'S' in line][0]
    n = start_line.find('S')
    img_bin[m * 2][n * 2] = 255
    direction = None

    i, j = 0, 0

    m, start_line = [(m, line) for m, line in enumerate(lines) if 'S' in line][0]
    n = start_line.find('S')
    i, j, direction = get_starting_node(m, n)
    m, n = m + i, n + j
    node = lines[m][n]

    while node != 'S':
        img_bin[m * 2][n * 2] = 255
        img_bin[m * 2 - i][n * 2 - j] = 255
        i, j, direction = moves[(node, direction)]
        m, n = m + i, n + j
        node = lines[m][n]
    img_bin[m * 2 - i][n * 2 - j] = 255
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_bin_cpy = img_bin.copy()
    cv2.drawContours(img_bin, contours, -1, 255, thickness=cv2.FILLED)
    img_bin -= img_bin_cpy

    #take only every second pixel to undo padding from before
    result_image = img_bin[::2, ::2]

    print(int(np.sum(result_image)/255))

if __name__ == '__main__':
    main()