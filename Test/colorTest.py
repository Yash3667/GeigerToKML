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

'''
def calcRed(radlvl):
	"""
	Calculates the level of Red

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	if radlvl <= trivialCPM:
		red = 0
	elif radlvl <= notableCPM:
		red = (radlvl - trivialCPM) * 255 // (notableCPM - trivialCPM)
	else:
		red = 255

	return hex(int(red))[2:].zfill(2)


def calcGreen(radlvl):
	"""
	Calculates the level of Green.

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	if radlvl <= notableCPM:
		green = 255
	elif radlvl <= mediumCPM:
		green = 255 - (radlvl - notableCPM) * 128 // (mediumCPM - notableCPM)
	elif radlvl <= highCPM:
		green = 128 - (radlvl - mediumCPM) * 128 // (highCPM - mediumCPM)
	else: 
		green = 0

	return hex(int(green))[2:].zfill(2)


def calcBlue(radlvl):
	"""
	Calculates the level of Blue

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	# No blue in Green, Yellow, or Red
	blue = 0
	return hex(int(blue))[2:].zfill(2)


def calcAlpha(radlvl):
	"""
	Calculates the level of Alpha

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	# Fully opaque
	alpha = 255
	return hex(alpha)[2:].zfill(2)
'''

lvl = 0
speed(0)
left(90)

while calcGreen(lvl) != "00":
	col = calcColor(lvl)
	drawLine(col)
	nextLine()
	lvl += 750

done()
