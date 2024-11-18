#imports
import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2,30,auto_write = False,brightness = .1)

#colors
red = (230,15,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,50,0)
cyan = (0,255,255)
magenta = (255,0,255)
pink = (255,53, 127)
purple = (76,4,153)
lightGreen = (70,247,70)
orange = (250,75,5)
darkGreen = (1, 40, 2)
white = (255,255,255)

#functions
def candyCane(color, color2):
    """
    simulates pattern of candy cane 

    parameters:
    color (tuple): the rgb sequence of a specific color
    color2 (tuple): the rgb sequence of a specific color

    returns:
    n/a

    authors:
    Miking and Fritz with assistance from Casey
    """
    count = 0
    for i in range(np.n):
        np.fill(color)
        for i in range(np.n):
            if (i + count) % 4 == 0:
                np[i] = color2
            if (i + count) % 4 == 1:
                np[i] = color2
        np.show()
        time.sleep(.2)
        count = (count + 1) % 3


#main
while True:
  candyCane(white, red)
