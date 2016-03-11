import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import turtle
import getopt

from Milestones import *
import Mapper



def drawSlice(r, g, b):
	"""
	Draws a slice of a specified color.
	Parameters:
	r 	(String): The Red component. 2 Hex digits
	g 	(String): The Green component. 2 Hex digits
	b 	(String): The Blue component. 2 Hex digits
	"""
	turtle.color("#" + r + g + b)
	turtle.forward(100)

def drawSlice(col):
	"""
	Draws a slice of the specified color.
	Parameters:
	col 	(String): An RGB string in the format '#RRGGBB'
	"""
	turtle.color(col)
	turtle.forward(100)

def nextSlice():
	"""
	Moves the turtle to the next slice.
	"""
	turtle.back(100)
	turtle.right(90)
	turtle.forward(1)
	turtle.left(90)

def nextLine():
	"""
	Moves the turtle to the next line.
	"""
	turtle.setx(-350)
	turtle.forward(100)


def calcColor(radlvl):
	"""
	Determines color based on Mapper.py's color 
	calculation functions.
	"""
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
		drawSlice(col)
		nextSlice()
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
		drawSlice(col)
		nextSlice()
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


def printUsage():
	"""
	Prints usage of script and exits.
	"""

	print "ColorTest [OPTIONS]\n"
	print "Options:\n"
	print "		-r 			Prints the real distribution of colors\n"
	print "		-n 			Prints a normalized distribution of colors\n"
	print "		-c 			Prints colors in colorblind mode\n"
	print "\nExample usage:"
	print "		ColorTest -r -c"
	print "		ColorTest -n"
	print "		ColorTest -n -r"

	sys.exit(0)


""" Script Execution """

try:
	opts, args = getopt.getopt(sys.argv[1:], "rnc", ["real", "normalized", "colorblind"])
except getopt.GetoptError as err:
	print str(err)
	printUsage()

if len(opts) == 0:
	printUsage()


turtle.speed(0)
turtle.setx(-350)
turtle.left(90)
setting = 0


for option, value in opts:
	if option == "-c":
		Mapper.colorBlind = True
	else:
		Mapper.colorBlind = False

	if option == "-r":
		setting += 1
	elif option == "-n":
		setting += 2

if setting >= 1:
	realDistribution()
	nextLine()
if setting >= 2:
	evenSpacing()


turtle.done()