'''
NOTE:	Nothing in here has been tested yet.

		The functions in this file depend on
		the following functions which are to 
		be implemented by Matthew:

		-makeMarker(coordinates, color code)
		-makePath(coordinate list, color code)

		The names for the above methods can be
		modified, they are simply suggestions.
'''

# NOTE:	These values are TEMPORARY, pending further investigation
medium	= 100
high	= 1000 
'''
The above variables are tunable parameters that control when
yellow is reached and when Red is reached (see calcRads and 
supporting functions for further details). They are measured
in CPM
'''

	
def mapData(data):
	'''
	Segments the path into mini-paths of varying colors
	(color dependent on radiation levels)
	'''

	# Handle strange cases
	if len(data) == 1:
		entry = data[0]
		radColor = calcRads(entry)
		makeMarker(getPoint(entry), radColor)

	while len(data) > 1:
		# Make a new path
		path = []

		# Calculate the radiation color of the path
		radOne = calcRads(data[0])
		radTwo = calcRads(data[1])

		radColor = (radOne + radTwo) // 2

		# Extract the lat and long and put them on the path
		path.append(data[0])
		del data[0]
		path.append(data[0])

		# Add additional points to the path, if applicable
		while len(data) > 1:
			path.append(data[0])

			if calcRads(data[1]) == radColor:
				del data[0]
			else:
				break

		makePath(path, radColor)



def getPoint(entry):
	'''
	Extracts the latitude and longitude from a data entry
	'''
	return [entry[4], entry[5]]



def calcRads(entry):
	'''
	This function is in charge of one of the most important parts:
	which color do we put on the map?

	Uses an ARGB color scheme in accordance with KML
	'''
	alpha = calcAlpha(entry[1])
	red = calcRed(entry[1])
	green = calcGreen(entry[1])
	blue = calcBlue(entry[1])
	return alpha + red + blue + green


'''
Colors range from Green (low radiation) to Red (high radiation),
with Yellow between them (medium radiation)
'''

def calcRed(radlvl):
	'''
	Calculates the level of Red
	Returns a 2 digit hexadecimal string
	'''
	if radlvl >= medium:
		red = 255
	else:
		red = radlvl * 255 // medium

	return hex(red)[2:].zfill(2)


def calcGreen(radlvl):
	'''
	Calculates the level of Green.
	Returns a 2 digit hexadecimal string
	'''
	if radlvl =< medium:
		green = 255
	else:
		green = (radlvl - medium) * 255 // high

	return hex(green)[2:].zfill(2)

def calcBlue(radlvl):
	'''
	Calculates the level of Blue
	Returns a 2 digit hexadecimal string
	'''
	# No blue in Green, Yellow, or Red
	blue = 0
	return hex(blue)[2:].zfill(2)

def calcAlpha(radlvl):
	'''
	Calculates the level of Alpha
	Returns a 2 digit hexadecimal string
	'''
	# Fully opaque
	alpha = 255
	return hex(alpha)[2:].zfill(2)