"""
NOTE:	Nothing in here has been tested yet.
		This file is not currently complete

		The functions in this file depend on
		the following functions which are to 
		be implemented by Matthew:

		-makeMarker(coordinates, color code)
		-makePath(coordinate list, color code)

		The names for the above methods can be
		modified, they are simply suggestions.
"""
import Milestones


trivialCPM 	= convertToCPM(trivialDose, trivialPeriod)
notableCPM 	= convertToCPM(notableDose, notablePeriod)
mediumCPM	= convertToCPM(mediumDose, mediumPeriod)
highCPM 	= convertToCPM(highDose, highPeriod)



def convertToCPM(dose, period):
	"""
	Converts from milliSieverts/hr to CPM 

	Parameters:
	dose 	(double): The dosage
	period 	(double): The time period over which the dosage4
					 is administered

	Returns the measurement in CPM
	"""
	conversionFactor = 350000 / 1.0
	return conversionFactor * dose / period



	
def mapData(data):
	"""
	Segments the path into mini-paths of varying colors
	(color dependent on radiation levels)

	Parameters:
	data 	(List): A list of parsed log entries
	"""

	# Handle datasets of a single entry
	if len(data) == 1:
		entry = data[0]
		radColor = calcRadColor(entry)
		makeMarker(getPoint(entry), radColor)

	while len(data) > 1:
		# Make a new path
		path = []

		# Calculate the radiation color of the path
		radOne = calcRadColor(data[0])
		radTwo = calcRadColor(data[1])

		radColor = avgRadColor(radOne, radTwo)

		# Extract the lat and long and put them on the path
		path.append(data[0])
		del data[0]
		path.append(data[0])

		# Add additional points to the path, if applicable
		while len(data) > 1:
			path.append(data[0])

			if calcRadColor(data[1]) == radColor:
				del data[0]
			else:
				break

		makePath(path, radColor)



def getPoint(entry):
	"""
	Extracts the latitude and longitude from a data entry

	Parameters:
	entry 	(List): A single parsed log entry
	"""
	return [entry[4], entry[5]]


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
	blue = hex(red)[2:].zfill(2)

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
	alpha 	= calcAlpha(int(entry[1]))
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
	if radlvl =< trivialCPM:
		red = 0
	elif radlvl <= mediumCPM:
		red = (radlvl - trivialCPM) * 255 // (notableCPM - trivialCPM)
	else:
		red = 255

	return hex(red)[2:].zfill(2)


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
		green = 256 - (radlvl - notableCPM) * 128 // (mediumCPM - notableCPM)
	else:
		green = 128 - (radlvl - mediumCPM) * 128 // (highCPM - mediumCPM)

	return hex(green)[2:].zfill(2)


def calcBlue(radlvl):
	"""
	Calculates the level of Blue

	Parameters:
	radlvl 	(int): The radiation level in CPM

	Returns a 2 digit hexadecimal string
	"""
	# No blue in Green, Yellow, or Red
	blue = 0
	return hex(blue)[2:].zfill(2)


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