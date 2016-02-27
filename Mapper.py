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


#chopping block
def getPoint(entry):
	"""
	Extracts the latitude and longitude from a data entry

	Parameters:
	entry 	(List): A single parsed log entry
	"""
	return [float(entry[5]), float(entry[6])]

#chopping block
def avgRadColor(radOne, radTwo):
	"""
	Averages two radiation colors.
	Decodes from an 8 digit hexademical ABGR string

	Parameters:
	radOne 	(String): A 32 bit ABGR hex string
	radTwo 	(String): A 32 bit ABGR hex string

	Returns an 8 digit hexadecimal ABGR string
	"""
	alpha = (int(radOne[:2], 16) + int(radTwo[:2], 16)) // 2
	alpha = hex(alpha)[2:].zfill(2)

	blue = (int(radOne[2:4], 16) + int(radTwo[2:4], 16)) // 2
	blue = hex(blue)[2:].zfill(2)

	green = (int(radOne[4:6], 16) + int(radTwo[4:6], 16)) // 2
	green = hex(green)[2:].zfill(2)

	red = (int(radOne[6:8], 16) + int(radTwo[6:8], 16)) // 2
	red = hex(red)[2:].zfill(2)
	
	return alpha + blue + green + red


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
		#red = 255 - 128 * (radlvl - trivialCPM) / (notableCPM - trivialCPM)
		k = -log(128.0/127 - 1) / notableCPM
		x = radlvl - trivialCPM
		red =  256 / (1 + exp(-1 * k * x)) # + 127
	elif radlvl <= mediumCPM:
		#red = 255 - 128 * (radlvl - notableCPM) / (mediumCPM - notableCPM)
		k = -log(128.0/127 - 1) / mediumCPM
		x = radlvl - notableCPM
		red = 256 / (1 + exp(-1 * k * x)) # + 127
	elif radlvl <= highCPM:
		#red = 255 - 128 * (radlvl - mediumCPM) / (highCPM - mediumCPM)
		k = -log(128.0/127 - 1) / highCPM
		x = radlvl - mediumCPM
		red = 256 / (1 + exp(-1 * k * x)) # + 127
	else:
		red = 127

	'''if radlvl <= trivialCPM:
		red = 0
	elif radlvl <= notableCPM:
		red = 192 + 64 * (radlvl- trivialCPM) / (notableCPM - trivialCPM)
	else:
		red = 255'''

	'''if radlvl <= trivialCPM:
		red = 0
	elif radlvl <= notableCPM:
		k = -log(128.0/127 - 1) / notableCPM
		x = radlvl - trivialCPM
		red = 256 / (1 + exp(-1 * k * x)) - 128
	elif radlvl > mediumCPM:
		k = -log(127.0/126 - 1) / mediumCPM
		x = radlvl - notableCPM
		red = 128 + 255 / (1 + exp(k * x))
	else:
		red = 255'''

	return hex(int(red))[2:].zfill(2)


def calcGreen(radlvl):
	"""
	Calculates the level of Green.

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	if radlvl <= trivialCPM:
		#green = 255 - 128 * radlvl / trivialCPM
		k = -log(128.0/127 - 1) / trivialCPM
		x = radlvl
		green = 256 / (1 + exp(-1 * k * x)) # + 127
	elif radlvl <= notableCPM:
		#green = 255 - 128 * (radlvl - trivialCPM) / (notableCPM - trivialCPM)
		k = -log(128.0/127 - 1) / notableCPM
		x = radlvl - trivialCPM
		green = 256 / (1 + exp(-1 * k * x)) # + 127
	elif radlvl <= mediumCPM:
		#green = 64 - 32 * (radlvl - notableCPM) / (mediumCPM - notableCPM)
		k = -log(32.0/31 - 1) / mediumCPM
		x = radlvl - notableCPM
		green = 64 / (1 + exp(-1 * k * x)) # + 31
	else:
		green = 0

	'''if radlvl <= notableCPM:
		green = 255
	elif radlvl <= mediumCPM:
		green = 192 - 64 * (radlvl - notableCPM) / (mediumCPM - notableCPM)
	elif radlvl <= highCPM:
		green = 64 - 64 * (radlvl - mediumCPM) / (highCPM - mediumCPM)
	else:
		green = 0'''

	'''#if radlvl <= trivialCPM:
	#	green = 255
	if radlvl <= notableCPM:
		green = 255
	elif radlvl <= mediumCPM:
		k = -log(255.0/254 - 1) / mediumCPM
		x = radlvl - notableCPM
		green = 510 / ( 1 + exp(k * x))
	else: 
		green = 0'''
	'''elif radlvl <= mediumCPM:
		k = -log(127.0/126 - 1) / mediumCPM
		x = radlvl - notableCPM
		green = 128 + 255 / (1 + exp(k * x))
	elif radlvl <= highCPM:
		k = -log(127.0/126 - 1) / highCPM
		x = radlvl - mediumCPM
		green = 255 / (1 + exp(k * x))'''
	

	return hex(int(green))[2:].zfill(2)


def calcBlue(radlvl):
	"""
	Calculates the level of Blue

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	'''if radlvl <= mediumCPM:
		blue = 0
	elif radlvl <= highCPM:
		k = -log(200.0/199 - 1) / highCPM
		x = radlvl - mediumCPM
		blue = 400 / (1 + exp(-1 * k * x)) - 200
	else:
		blue = 255'''
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