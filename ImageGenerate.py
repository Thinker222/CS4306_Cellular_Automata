from PIL import Image
import numpy as np
import sys
import imageio

def createimage(arr):
    arr = np.flip(arr, axis=1).T
    sh = arr.shape
    img = Image.new('RGB', (sh[0], sh[1]))
    pixels = img.load()
    for row in range(sh[0]):
        for col in range(sh[1]):
            num = 255
            if arr[row][col] == 1:
                num = 0
            pixels[row, col] = (num, num, num)
    img.show()

def create_gif(history):
    images = []
    for arr in history:
        arr = np.flip(arr, axis=1).T
        sh = arr.shape
        img = Image.new('RGB', (sh[0], sh[1]))
        pixels = img.load()
        for row in range(sh[0]):
            for col in range(sh[1]):
                num = 255
                if arr[row][col] == 1:
                    num = 0
                pixels[row, col] = (num, num, num)
        images.append(arr)
    imageio.mimsave("stuff.gif", images, duration=1)