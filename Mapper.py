from Milestones import *
from KMLWriter import *
from math import *


def mapData(data):
	"""
	Segments the path into mini-paths of varying colors
	(color dependent on radiation levels)

	Parameters:
	data 	(List): A list of parsed log entries
	"""
	#should we put a placemarker for the beginning? we don't know where it comes from.....
	#other option: don't show data without a valid radiation flag. a valid radiation flag guarantees 1 minute of previous entries

	'''# Skip data with an invalid radiation flag
	# One invalid entry is left for beginning coordinates of the path
	while len(data) > 1 and data[1][4] == "V":
		del data[0]'''

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

		makeLine(path, radColor, radlvl)


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

	if radlvl <= trivialCPM:
		red = 0
	elif radlvl <= notableCPM:
		k = -log(128.0/127 - 1) / notableCPM
		x = radlvl - trivialCPM
		red =  256 / (1 + exp(-1 * k * x)) 
	elif radlvl <= mediumCPM:
		k = -log(128.0/127 - 1) / mediumCPM
		x = radlvl - notableCPM
		red = 256 / (1 + exp(-1 * k * x)) 
	elif radlvl <= highCPM:
		k = -log(128.0/127 - 1) / highCPM
		x = radlvl - mediumCPM
		red = 256 / (1 + exp(-1 * k * x)) 
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
	if radlvl <= trivialCPM:
		k = -log(128.0/127 - 1) / trivialCPM
		x = radlvl
		green = 256 / (1 + exp(-1 * k * x))
	elif radlvl <= notableCPM:
		k = -log(128.0/127 - 1) / notableCPM
		x = radlvl - trivialCPM
		green = 256 / (1 + exp(-1 * k * x))
	elif radlvl <= mediumCPM:
		k = -log(32.0/31 - 1) / mediumCPM
		x = radlvl - notableCPM
		green = 64 / (1 + exp(-1 * k * x)) # + 31
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
	blue = 00
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