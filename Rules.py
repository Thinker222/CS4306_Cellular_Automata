import numpy as np

def wolfram(arr, rule=1):
    rule_convert = '{0:08b}'.format(rule)
    new_arr = np.zeros(arr.shape)
    new_arr[0] = arr[0]
    for row in range(1,arr.shape[0]):
        for col in range(arr.shape[1]):
            new_arr[row][col] = (int)(rule_convert[wolframgetindex(arr, row, col)])
    return new_arr

def wolframgetindex(arr, row, col):
    if row == 0:
        return 0
    up = arr[row - 1][col]
    up_right = up
    up_left = up
    if col - 1 >= 0:
        up_left = arr[row - 1][col - 1]
    up = arr[row - 1][col]
    if col + 1 < arr.shape[1]:
        up_right = arr[row - 1][col + 1]
    num = 7 - (int)((1 * up_left) + (2 * up) + (4 * up_right))
    return num

def conway(arr, rule = '23/3'):
    new_arr = np.zeros(arr.shape)
    survive = []
    birth = []
    find_survive = True
    for ch in rule:
        if ch.isdigit():
            if find_survive:
                survive.append(int(ch))
            else:
                birth.append(int(ch))
        else:
            find_survive = False
    apply_conway(arr, new_arr, survive, birth)
    return new_arr

def apply_conway(arr, new_arr, survive, birth):
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            up_left = 0
            up = 0
            up_right = 0
            right = 0
            down_right = 0
            down = 0
            down_left = 0
            left = 0
            if row - 1 >= 0:
                up = arr[row - 1][col]
                if col - 1 >= 0:
                    up_left = arr[row - 1][col - 1]
                    left = arr[row][col - 1]
                if col + 1 < arr.shape[1]:
                    up_right = arr[row - 1][col - 1]
                    right = arr[row][col + 1]
            if row + 1 < arr.shape[0]:
                down = arr[row + 1][col]
                if col - 1 >= 0:
                    down_left = down_left = arr[row + 1][col - 1]
                if col + 1 < arr.shape[1]:
                    down_right = arr[row + 1][col + 1]
            total_neighbors = up_left + up + up_right + right + down_right + down + down_left + left
            if int(total_neighbors) in birth:
                new_arr[row][col] = 1
            elif total_neighbors in survive:
                new_arr[row][col] = arr[row][col]
            else:
                new_arr[row][col] = 0

def setup_conway(arr):
    sh = arr.shape
    origin = (sh[0] // 2, sh[1] // 2)
    glider=[
        [1,1,0,1],
        [1,0,1,1]
    ]
    for x  in range(len(glider)):
        for y in range (len(glider[x])):
            arr[origin[0] + x][origin[1] + y] = glider[x][y]