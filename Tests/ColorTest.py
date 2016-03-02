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


# Regular
Mapper.colorBlind = False
lvl = 0
turtle.speed(0)
turtle.setx(-350)
turtle.clear()
turtle.left(90)

while lvl <= highCPM:
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	if lvl <= trivialCPM:
		lvl += trivialCPM / 100
	elif lvl <= notableCPM:
		lvl += (notableCPM - trivialCPM) / 100
	elif lvl <= mediumCPM:
		lvl += (mediumCPM - notableCPM) / 100
	else:
		lvl += (highCPM - mediumCPM) / 100
	

#ColorBlind
Mapper.colorBlind = True
lvl = 0
turtle.setx(-350)
turtle.sety(100)

while lvl <= highCPM:
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	if lvl <= trivialCPM:
		lvl += trivialCPM / 100
	elif lvl <= notableCPM:
		lvl += (notableCPM - trivialCPM) / 100
	elif lvl <= mediumCPM:
		lvl += (mediumCPM - notableCPM) / 100
	else:
		lvl += (highCPM - mediumCPM) / 100

turtle.done()