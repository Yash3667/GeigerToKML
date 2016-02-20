import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


from turtle import *
from Milestones import *
from Mapper import *



def drawLine(r, g, b):
	color("#" + r + g + b)
	forward(100)

def drawLine(col):
	color(col)
	forward(100)

def nextLine():
	back(100)
	right(90)
	forward(1)
	left(90)



def calcColor(radlvl):
	red 	= calcRed(radlvl)
	green 	= calcGreen(radlvl)
	blue 	= calcBlue(radlvl)
	return "#" + red + green + blue



lvl = 0
speed(0)
left(90)

while calcGreen(lvl) != "00":
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	lvl += 750

done()
