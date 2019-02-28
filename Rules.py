import numpy as np

# This is the wolfram rule
# You pass in a numpy array and a tuple containing an integer that defines the rule and a bool that describes whether
# or not the Wolfram algorithm will "cheat"
def wolfram(arr, rule=(1,False)):
    # We get the actual rule number
    actual_rule = rule[0]
    # We get the boolean that decides whether or not it cheats
    # When wolfram's algorithm runs, a new row will be populated with each iteration
    # However, once a row is populated, its values will not change
    # Therefore, instead of running through all of the rows over and over for several
    # generations, we can "cheat" and update all of the rows at once. This will make the algorithm run faster
    # and create a usable output faster in O(n^2) time instead of O(n^3) time -> n dim X n Dim X n Dim as opposed to just
    # n Dim X nDim.
    cheat = rule[1]
    rule_convert = '{0:08b}'.format(actual_rule)
    new_arr = np.zeros(arr.shape)
    new_arr[0] = arr[0]
    for row in range(1,arr.shape[0]):
        for col in range(arr.shape[1]):
            if(cheat):
                new_arr[row][col] = (int)(rule_convert[wolframgetindex(new_arr, row, col)])
            else:
                new_arr[row][col] = (int)(rule_convert[wolframgetindex(arr, row, col)])
    return new_arr


# This is a support function for wolfram.
# It looks at the values above to the left, above, and above to the right
# of the current row and column in the array.
# It then translates these three discrete values into a number
# between 0 and 7 inclusive.
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
    num = -1
    if up_left == 1 and up == 1 and up_right == 1:
        num = 0
    elif up_left == 1 and up == 1 and up_right == 0:
        num = 1
    elif up_left == 1 and up == 0 and up_right == 1:
        num = 2
    elif up_left == 1 and up == 0 and up_right == 0:
        num = 3
    elif up_left == 0 and up == 1 and up_right == 1:
        num = 4
    elif up_left == 0 and up == 1 and up_right == 0:
        num = 5
    elif up_left == 0 and up == 0 and up_right == 1:
        num = 6
    else:
        num = 7
    return  num

# Conway takes a rule as a string. The concatenated numbers before the '/' represent
# the survival numbers, and the numbers after the '/' represent the birth numbers.
def conway(arr, rule = '23/3'):
    new_arr = np.zeros(arr.shape)
    survive = []
    birth = []
    find_survive = True
    # Find the survival and birth numbers
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

# apply_conway updates the new_arr using the survival and birth rules with the arr array as input.
def apply_conway(arr, new_arr, survive, birth):
    # Itereate through every cell
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            # set all the 8 surrounding spots as 0
            up_left = 0
            up = 0
            up_right = 0
            right = 0
            down_right = 0
            down = 0
            down_left = 0
            left = 0
            # Update the 8 surrounding values if they exist
            if row - 1 >= 0:
                up = arr[row - 1][col]
                if col - 1 >= 0:
                    up_left = arr[row - 1][col - 1]
                    left = arr[row][col - 1]
                if col + 1 < arr.shape[1]:
                    up_right = arr[row - 1][col + 1]
                    right = arr[row][col + 1]
            if row + 1 < arr.shape[0]:
                down = arr[row + 1][col]
                if col - 1 >= 0:
                    down_left = down_left = arr[row + 1][col - 1]
                    left = arr[row][col - 1]
                if col + 1 < arr.shape[1]:
                    down_right = arr[row + 1][col + 1]
                    right = arr[row][col + 1]
            total_neighbors = up_left + up + up_right + right + down_right + down + down_left + left
            if(total_neighbors > 0):
                stuf = 2
            if int(total_neighbors) in birth and arr[row][col] != 1:
                new_arr[row][col] = 1
            elif int(total_neighbors) in survive:
                new_arr[row][col] = arr[row][col]
            else:
                new_arr[row][col] = 0

# Sets up the conway grid with a simple structure
def setup_conway(arr, creature):
    sh = arr.shape
    origin = (sh[0] // 2, sh[1] // 2)
    for x  in range(len(creature)):
        for y in range (len(creature[x])):
            arr[origin[0] + x][origin[1] + y] = creature[x][y]