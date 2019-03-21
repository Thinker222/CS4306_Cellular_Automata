from PIL import Image
import numpy as np
import sys
import imageio

# Creates and displays an image of the automata
# How Image works https://pillow.readthedocs.io/en/stable/reference/Image.html


def createimage(arr, rule, name = 'file'):
    arr = np.flip(arr, axis=1).T
    sh = arr.shape
    dim = max(sh[0], sh[1])
    img = Image.new('RGB', (sh[0], sh[1]))
    pixels = img.load()
    for row in range(sh[0]):
        for col in range(sh[1]):
            num = 255
            if arr[row][col] == 1:
                num = 0
            pixels[row, col] = (num, num, num)
    img.save(name)

# Creates and displays a gif of the automata
# You can change the duration to make the gif go faster or slower
# 1 or 2 for analysis; .2 to get a fast movie
# How to create gif in python https://imageio.readthedocs.io/en/latest/userapi.html?highlight=mimwrite (originally
#  found how to do this stack overflow post, but I could not find the post)
# Some of the args that are needed for this function:
#  https://imageio.readthedocs.io/en/stable/format_gif-pil.html#gif-pil


def create_gif(history, speed = .2, file = 'name.gif'):
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
        img = img.resize(size=(512, 512))
        images.append(img)
    imageio.mimwrite(file, images, duration=float(speed))