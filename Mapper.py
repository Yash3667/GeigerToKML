"""
NOTE:	Nothing in here has been tested yet.

		The functions in this file depend on
		the following functions which are to 
		be implemented by Matthew:

		-makeMarker(coordinates, color code)
		-makePath(coordinate list, color code)

		The names for the above methods can be
		modified, they are simply suggestions.
"""

# NOTE:	These values are TEMPORARY, pending further investigation
#notableDose	= 
#notablePeriod	= 

#mediumDose		=
#mediumPeriod	=

#highDose		=
#highPeriod		=
"""
The above variables are tunable parameters that control when
milestone colors are reached (see documentation for further 
details). 
"""

	
def mapData(data):
	"""
	Segments the path into mini-paths of varying colors
	(color dependent on radiation levels)

	Parameters:
	data (List): A list of parsed log entries
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
	entry (List): A single parsed log entry
	"""
	return [entry[4], entry[5]]


def avgRadColor(radOne, radTwo):
	"""
	Averages two radiation colors.
	Decodes from a 32 bit ARGB color scheme

	Parameters:
	radOne (String): A 32 bit ARGB hex string
	radTwo (String): A 32 bit ARGB hex string

	Returns an 8 digit hexadecimal ARGB string
	"""
	alpha = (int(radOne[:2], 16) + int(radTwo[:2], 16)) // 2
	alpha = hex(alpha)[2:].zfill(2)

	red = (int(radOne[2:4], 16) + int(radTwo[2:4], 16)) // 2
	red = hex(red)[2:].zfill(2)

	green = (int(radOne[4:6], 16) + int(radTwo[4:6], 16)) // 2
	green = hex(green)[2:].zfill(2)

	blue = (int(radOne[6:8], 16) + int(radTwo[6:8], 16)) // 2
	blue = hex(blue)[2:].zfill(2)
	
	return alpha + red + blue + green


def calcRadColor(entry):
	"""
	Calculates the color for a given 

	Uses a 32 bit ARGB color scheme in accordance with KML

	Parameters:
	entry (List): A single parsed log entry
	"""
	alpha 	= calcAlpha(int(entry[1]))
	red 	= calcRed(int(entry[1]))
	green	= calcGreen(int(entry[1]))
	blue	= calcBlue(int(entry[1]))
	return alpha + red + blue + green


"""
Colors range from Green (low radiation) to Red (high radiation),
with Yellow between them (medium radiation)
"""

def calcRed(radlvl):
	"""
	Calculates the level of Red
	Returns a 2 digit hexadecimal string

	Parameters:
	radlvl (int): The radiation level in CPM
	"""
	if radlvl >= medium:
		red = 255
	else:
		red = radlvl * 255 // medium

	return hex(red)[2:].zfill(2)


def calcGreen(radlvl):
	"""
	Calculates the level of Green.
	Returns a 2 digit hexadecimal string

	Parameters:
	radlvl (int): The radiation level in CPM
	"""
	if radlvl =< medium:
		green = 255
	else:
		green = (radlvl - medium) * 255 // high

	return hex(green)[2:].zfill(2)


def calcBlue(radlvl):
	"""
	Calculates the level of Blue
	Returns a 2 digit hexadecimal string

	Parameters:
	radlvl (int): The radiation level in CPM
	"""
	# No blue in Green, Yellow, or Red
	blue = 0
	return hex(blue)[2:].zfill(2)


def calcAlpha(radlvl):
	"""
	Calculates the level of Alpha
	Returns a 2 digit hexadecimal string

	Parameters:
	radlvl (int): The radiation level in CPM
	"""
	# Fully opaque
	alpha = 255
	return hex(alpha)[2:].zfill(2)