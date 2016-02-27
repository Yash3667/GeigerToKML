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
setx(-350)
clear()
left(90)

factor = 0
factorfactor = 0
while lvl < 350000:#calcBlue(lvl) != "ff":
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	#lvl += 750
	#c += 1
	#if c > 5:
	lvl += factor
	factor += factorfactor
	factorfactor += 0.1
	

'''
while lvl <= mediumCPM:
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	lvl  += 100

sety(100)
setx(-350)

while calcBlue(lvl) != "ff":
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	lvl  += 750
	'''

done()
