from math import *

from Milestones import *
import KMLWriter

global colorBlind
# A base case
colorBlind = False

def mapData(data):
	"""
	Segments the path into mini-paths of varying colors
	(color dependent on radiation levels)

	Parameters:
	data 	(List): A list of parsed log entries
	"""


	while len(data) > 1:
		# Make a new path
		path = []

		# Set the initial points
		path.append(data[0])
		del data[0]
		path.append(data[0])

		# Determine the radiation level of the path
		radlvl = data[0][1]

		# Calculate the radiation color of the path
		radColor = calcRadColor(data[0])


		# Add additional points to the path, if applicable
		while len(data) > 1:
			if data[1][0] == radlvl:
				del data[0]
				path.append(data[0])
			else:
				break

		KMLWriter.makeLine(path, radColor, radlvl)


def calcRadColor(entry):
	"""
	Calculates the color for a given entry
	Uses a 32 bit ABGR color scheme in accordance with KML

	Parameters:
	entry 	(List): A single parsed log entry

	Returns an 8 digit hexadecimal ABGR string
	"""
	alpha 	= calcAlpha(entry)
	red 	= calcRed(int(entry[1]))
	green	= calcGreen(int(entry[1]))
	blue	= calcBlue(int(entry[1]))
	return alpha + blue + green + red


"""
See documentation for details about color calculations
"""

def calcRed(radlvl):
	"""
	Calculates the level of Red

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	if colorBlind:
		if radlvl <= trivialCPM:
			red = 230
		elif radlvl <= mediumCPM:
			red = 253
		elif radlvl <= highCPM:
			red = 178
		else:
			red = 94

	else:
		if radlvl <= trivialCPM:
			red = 0
		elif radlvl <= mediumCPM:
			x = radlvl - trivialCPM	
			theta = x * radians(180)/ (mediumCPM - trivialCPM)
			red = 191 - 64 * cos(theta)
		elif radlvl <= highCPM:
			x = radlvl - mediumCPM
			theta = x * radians(180) / (highCPM - mediumCPM)
			red = 191 - 64 * cos(theta)
		elif radlvl <= veryHighCPM:
			x = radlvl - highCPM
			theta = x * radians(180) / (veryHighCPM - highCPM)
			red = 191 - 64 * cos(theta)
		else:
			red = 127

	return hex(int(red))[2:].zfill(2)


def calcGreen(radlvl):
	"""
	Calculates the level of Green.

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	if colorBlind:
		if radlvl <= trivialCPM:
			green = 97
		elif radlvl <= mediumCPM:
			green = 184
		elif radlvl <= highCPM:
			green = 171
		else:
			green = 60


	else:
		if radlvl <= trivialCPM:
			x = radlvl
			theta = x * radians(180) / trivialCPM
			green = 191 - 64 * cos(theta)
		elif radlvl <= mediumCPM:
			x = radlvl - trivialCPM
			theta = x * radians(180)/ (mediumCPM - trivialCPM)
			green = 191 - 64 * cos(theta)
		elif radlvl <= highCPM:
			x = radlvl - mediumCPM
			theta = x * radians(180)/ (highCPM - mediumCPM)
			green = 64 - 16 * cos(theta)
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
	if colorBlind:
		if radlvl <= trivialCPM:
			blue = 1
		elif radlvl <= mediumCPM:
			blue = 99
		elif radlvl <= highCPM:
			blue = 210
		else:
			blue = 153

	else:
		if radlvl < veryHighCPM:
			blue = 00
		else:
			blue = 255
	return hex(int(blue))[2:].zfill(2)


def calcAlpha(entry):
	"""
	Calculates the level of Alpha

	Parameters:
	entry	(List): A parsed data entry

	Returns a 2 digit hexadecimal string
	"""
	# If either validity flag is void, represent with 50% transparency
	# Otherwise, the path should be fully opaque
	if entry[4] == "V" or entry[8] == "V":
		alpha = 64
	else:
		alpha = 255
	return hex(alpha)[2:].zfill(2)