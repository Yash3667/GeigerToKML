from math import *
import re
import datetime

from Milestones import *
import KMLWriter


global colorBlind
# A base case
colorBlind = False

mu = unichr(956)

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

		# Verify that the points are from a consecutive time interval
		if compareTimes(path[0][0], path[1][0]) != 5:
			# If not, continue from the next possible path
			continue

		# Verify GPS validity flag
		if path[0][8] == 'V' or path[1][8] == 'V':
			# If invalid, continue from next possible path
			continue


		# Determine the radiation level of the path in CPM
		radlvl = data[0][1]


		# Calculate the radiation color of the path
		radColor = calcRadColor(data[0])


		# Add additional points to the path, if applicable
		while len(data) > 1:
			if data[0][1] == radlvl and data[0][8] != 'V':
				del data[0]
				path.append(data[0])
			else:
				break

		# Add units and equivalent measurements
		uSvPerHr = CPMTomSvPerHr(int(radlvl))
		Bq = CPMToBq(int(radlvl))
		uRemPerHr = CPMToRemPerHr(int(radlvl))
		radlvl = str(radlvl) + " CPM"
		radlvl = (radlvl, uSvPerHr, Bq, uRemPerHr)

		# Send the path off to be added to the KML
		KMLWriter.makeLine(path, radColor, radlvl)

def compareTimes(t1, t2):
    """
    Computes the difference in seconds of two times given in the
    log.

    Parameters
    t1	(String): First UTC time according to the log
    t2	(String): Second UTC time according the log
    """

    # Split the given times and create timedates for each of them
    utcSplit1 = re.split('\D', t1)
    for i in range(0, 6):
    	utcSplit1[i] = int(utcSplit1[i])
    utcTime1 = datetime.datetime(utcSplit1[0], utcSplit1[1], utcSplit1[2], utcSplit1[3],  utcSplit1[4], utcSplit1[5])

    utcSplit2 = re.split('\D', t2)
    for i in range(0, 6):
    	utcSplit2[i] = int(utcSplit2[i])
    utcTime2 = datetime.datetime(utcSplit2[0], utcSplit2[1], utcSplit2[2], utcSplit2[3],  utcSplit2[4], utcSplit2[5])

    return (utcTime2 - utcTime1).total_seconds()

def CPMTomSvPerHr(cpm):
	"""
	Converts from CPM to microSieverts/hr

	Parameters:
	cpm 	(int): Counts per minute

	Returns the measurement in microSieverts/hr
	as a string with units.
	"""
	uSvPerHr = cpm * 1.0 / 350
	return str(uSvPerHr) + " " + mu + "Sv/hr"

def CPMToBq(cpm):
	"""
	Converts from CPM to Becquerel

	Parameters:
	cpm 	(int): Counts per minute

	Returns the measurement in Becquerels
	as a string with units.
	"""
	cps = cpm / 60.0
	return str(cps) + " Bq"

def CPMToRemPerHr(cpm):
	"""
	Converts from CPM to microRem/hr

	Parameters:
	cpm 	(int): Counts per minute

	Returns the measurement in microRem/hr
	as a string with units
	"""
	# Convert from CPM to microSv/hr, then to microRem/hr
	uSvPerHr = cpm * 1.0 / 350
	uRemPerHr = uSvPerHr * 0.1
	return str(uRemPerHr) + " " + mu + "Rem/hr"



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
			green = 80 - 16 * cos(theta)
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
	# If radcount validity flag is invalid, represent with 75% transparency
	# Otherwise, the path should be fully opaque
	if entry[4] == "V":
		alpha = 64
	else:
		alpha = 255
	return hex(alpha)[2:].zfill(2)