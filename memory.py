import random, sys
import pygame as pg

#constants
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 40
GAPSIZE = 10    
BOARDWIDTH = 10
BOARDHEIGHT = 7
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

# R G B
GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

# initializing pygame window
pg.init()
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

xm = 0 # to store x coordinate of mouse 
ym = 0 # to store y coordinate of mouse
pg.display.set_caption("Memory Game")


def generateRevealedBoxesData(val): # make board of false to detect the revealed easly
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    # Get all shapes an colors
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )
    random.shuffle(icons) # randomize the order
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    board = []
    for x in range(BOARDWIDTH):
        column =[]
        for y in range(BOARDHEIGHT):
            column.append(icons[0]) # add icon from list
            del icons[0] # del used icon
        board.append(column)
    return board

mainBoard = getRandomizedBoard()
revealedBoxes = generateRevealedBoxesData(False)

