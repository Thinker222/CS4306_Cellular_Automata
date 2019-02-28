import numpy as np
from Rules import wolfram, conway, setup_conway
from ImageGenerate import createimage, create_gif
from Creatures import creatures
'''
A cellular automata is displayed using a grid. 
The contents of the grid are defined from iteration tjo iteration using rules. 
The Automoata class takes a x_size and a y_size (these get flipped in the final product) 
It also takes a rule function. There is a default norule function that does nothing, but other useful rules can be found in Rules.py
It takes a function that sets up the grid. There is a default rule called default_setup, but more setups can be found and defined in Rules.py
The update function updates the automato grid a specified number of times
The print function displays the current state of the automata. 
The print_movie function creates a gif using the history of the automata.
'''

# Default rule for automata; does not do anything useful
def norule(arr, par):
    return arr

# Defualt setup rule for automata; good for wolfram implementations
def default_setup(arr):
    sh = arr.shape
    arr[0][sh[1] // 2] = 1


# The automata class
class Automata:
    def __init__(self, x_size = 250, y_size = 500, rule = norule, par = None, setup = default_setup, setup_params = None):
        self.__x_size = x_size
        self.__y_size = y_size
        self.__rule = rule
        self.__par = par
        self.__setup = setup
        self.__setup_params = setup_params
        self.__grid = np.zeros(shape=(x_size, y_size))
        self.__history = []

# Calls the setup function that was initially passed in
    def setup(self):
        if self.__setup_params == None:
            self.__setup(self.__grid)
        else:
            self.__setup(self.__grid, self.__setup_params)


# Updates the automata a specified number of times using the rule function that was passed in.
# The last state is also appended to a history
    def update_automata(self, times = 1):
        for time in range(times):
            self.__history.append(self.__grid)
            self.__grid = self.__rule(self.__grid, self.__par)

# The print function creates and shows an image of the current automata grid
    def print(self, name = 'file.jpg'):
        createimage(self.__grid, self.__par, name)

# This function creates and saves a gif of the current automata (You may need to zoom in on it)
    def print_movie(self, speed = .2, name = 'file.gif'):
        create_gif(self.__history, speed, name)


# Some example code (a main function will be developed later)
#for i in range(0,256):
#    aut = Automata(rule = wolfram, par=(i,True), setup = default_setup)
#    aut.setup()
#    aut.update_automata(times = 1)
#    aut.print()

#aut = Automata(rule = conway, x_size= 80, y_size= 80, par='23/3', setup = setup_conway, setup_params=creatures['F-pentomino'])
#aut.setup()
#aut.update_automata(times=1500)
#aut.print_movie('penton2.gif')