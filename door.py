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
gray = (100,100,100)
black = (0,0,0)

#variables
lsts = [red, white,green]
lst = [white,white,white]
y = 0

#main functions
#ONLY ADD FUNCTIONS THAT ARE CALLED IN THE MAIN LOOP

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
        time.sleep(.12)
        count = (count + 1) % 3

def snowfall():
    """
    This fills up the entire strip with a chosen color
    
    parameters:
    n/a
    
    returns:
    n/a
    
    authors:
    Oly & Jacobi
    """
    for i in range(np.n -1, -1, -1):
        if (i == i-2) % 3 == 0:
            sign = i // 2
            if i < np.n // 2:
                np[sign] = white
            sine = i // -2
            if i > np.n // - 2:
                np[sine] = white
            np[i] = white
            np.show()
            time.sleep(0.1)
        if (i == i+2) % 3 == 0:
            if i > np.n // -2:
                np[sine] = white
    count = 0
    for x in range(np.n):
        if x < np.n // 3:
            for x in range(np.n):
                if (x + count) % 3 == 0:
                    np[x] = (black)
        time.sleep(0.2)
        np.show()
        count = (count + x) % 3


def dots(dotColor = darkGreen, black = (0,0,0), endColor = red, i = 0, b = (np.n - 1), timesleep = 0.1, count = 0):
    """
    two dots meet halfway in the center then once cross paths they fill the neopixels with the endColor as they reach the ends
    
    parameters:
    dotColor (tuple): the rgb sequence of a specific color: set to darkGreen
    black (tuple): the rgb sequence of a specific color: set to (0,0,0)
    endColor (tuple): the rgb sequence of a specific color: set to red
    i (int): set to 0
    b (int): set to # of pixels - 1
    timesleep (double): set to 0.03
    count (int): set to 0
    
    returns:
    n/a

    authors:
    Casey & Dana 
    """
    global y
    for x in range(np.n):
        np[i] = (dotColor)
        np[(i - 1) % np.n] = black
        i = (i + 1) % np.n
        
        
        np[b] = (dotColor)
        np[(b + 1) % np.n] = black
        b = (b - 1) % np.n
        
        np.show()
        time.sleep(timesleep) 
        if(i == (np.n / 2)):
            for l in range(np.n - 1):
                if l % 2 == 0:
                    np[l] = red
                else:
                    np[l] = green
            time.sleep(2)
            np.show()

        if(y % 2 == 1):
            black = (0,0,0)
            dotColor = darkGreen
            
        
    wipe(red)
    for i in range(13):
        sparkle(red, white, 0.015, 5)
    np.fill(red)
    time.sleep(0.2)
    reverseWipe(green)
    for i in range(13):
        sparkle(green, white, 0.015, 5)
    np.fill(green)
    time.sleep(0.2)


def lightWork():
    """
    This is the set of code that will show christmas lightwork on the leds. Fritz made this
    
    parameters:
    n/a 

    returns:
    n/a

    authors:
    Fritz & Miking
    """
    chase1(lsts)
    reverse_wipe(lst)
    reverse_wipe(lsts)


#inside functions
#ONLY ADD FUNCTIONS THAT ARE CALLED IN OTHER FUNCTIONS HERE
def wipe(color):
    """
    docstrings will be added!
    """
    for i in range(np.n):
        np[i] = color
        np.show()
        time.sleep(0.06)
        
def reverseWipe(color):
    """
    docstrings will be added!
    """
    for i in range(np.n - 1, -1, -1):
        np[i] = color
        np.show()
        time.sleep(0.06)
        
def sparkle(baseColor, sparkleColor, speed, numSpark):
    """
    simulates a sparkling effect with a solid background
    
    parameters:
    baseColor (tuple): the rgb sequence of a specific color
    sparkleColor (tuple): the rgb sequence of a specific color
    numSpark (int): number of sparkles shown
    speed (double): the speed at which the sparkles show: set to 0.015
    
    returns:
    n/a

    authors:
    Dana
    """
    np.fill(baseColor)                                                                                           
    for i in range(numSpark):
        y = random.randint(0, (np.n -1))
        np[y] = sparkleColor
        time.sleep(speed)
    np.show()

def chase1(colors):
    """
    docstrings will be added!
    """
    for i in range(np.n):
        np[i] = colors[i%len(colors)]
        np.show()
        time.sleep(0.04)
    
def reverse_wipe(colors):
    """
    Reverse_wipe will be used to wipe chase1 depending on the list of colors

    parameters:
    colors(list): a list containing tuples of rgb color sequences

    returns:
    n/a

    authors:
    Fritz & Miking
    """
    for i in range(np.n):
        i = i* -1
        np[i] = random.choice(colors)
        np.show()
        time.sleep(0.04)


#main
while True:
    candyCane(white, red)
    dots()
    snowfall()
    lightWork()
