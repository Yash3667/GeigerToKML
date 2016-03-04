import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import turtle

from Milestones import *
import Mapper



def drawLine(r, g, b):
	turtle.color("#" + r + g + b)
	turtle.forward(100)

def drawLine(col):
	turtle.color(col)
	turtle.forward(100)

def nextLine():
	turtle.back(100)
	turtle.right(90)
	turtle.forward(1)
	turtle.left(90)



def calcColor(radlvl):
	red 	= Mapper.calcRed(radlvl)
	green 	= Mapper.calcGreen(radlvl)
	blue 	= Mapper.calcBlue(radlvl)
	return "#" + red + green + blue


def realDistribution():
	"""
	Prints the real distribution of the 
	colors.
	"""
	lvl = 0

	while lvl <= veryHighCPM + 15000:
		col = calcColor(lvl)
		drawLine(col)
		nextLine()
		lvl += 750

def evenSpacing():
	"""
	Prints a distribution of the colors 
	where each color has roughly the same 
	number of slices allocated to it.
	"""
	lvl = 0

	while lvl <= veryHighCPM + 100:
		col = calcColor(lvl)
		drawLine(col)
		nextLine()
		if lvl <= trivialCPM:
			lvl += trivialCPM / 100
		elif lvl <= mediumCPM:
			lvl += (mediumCPM - trivialCPM) / 100
		elif lvl <= highCPM:
			lvl += (highCPM - mediumCPM) / 100
		elif lvl <= veryHighCPM:
			lvl += (veryHighCPM - highCPM) / 100
		else:
			lvl += 1


turtle.speed(0)

# Regular
Mapper.colorBlind = False
turtle.setx(-350)
turtle.left(90)
evenSpacing()
	

#ColorBlind
Mapper.colorBlind = True
turtle.setx(-350)
turtle.sety(100)
evenSpacing()

turtle.done()


"""
For later development: add option capability for
easy usage without modifying code.
"""