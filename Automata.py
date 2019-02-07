import numpy as np
from Rules import wolfram, conway, setup_conway
from ImageGenerate import createimage, create_gif
def norule(arr, par):
    return arr

def default_setup(arr):
    sh = arr.shape
    arr[0][sh[1] // 2] = 1


class Automata:
    def __init__(self, x_size = 10, y_size = 10, rule = norule, par = 1, setup = default_setup):
        self.__x_size = x_size
        self.__y_size = y_size
        self.__rule = rule
        self.__par = par
        self.__setup = setup
        self.__grid = np.zeros(shape=(x_size, y_size))
        self.__history = []


    def Setup(self):
        self.__setup(self.__grid)

    def update_automata(self, times = 1):
        for time in range(times):
            self.__history.append(self.__grid)
            self.__grid = self.__rule(self.__grid, self.__par)

    def print(self):
        createimage(self.__grid)
        create_gif(self.__history)


aut = Automata(rule = conway, par='23/3', setup = setup_conway)
aut.Setup()
aut.update_automata(times = 200)
aut.print()