"""
These variables are tunable parameters that control when
milestone colors are reached (see documentation for further 
details). 
"""

# Trivial corresponds to Green
trivialDose 	= 3
trivialPeriod	= 24 * 365

# Notable corresponds to Yellow
notableDose		= 130
notablePeriod	= 24 * 365

# Medium corresponds to Orange
mediumDose		= 700
mediumPeriod	= 24 * 365

# High corresponds to Red
highDose		= 170
highPeriod		= 24 * 7



"""
Do not edit code below this line.
"""
def convertToCPM(dose, period):
	"""
	Converts from milliSieverts/hr to CPM 

	Parameters:
	dose 	(double): The dosage
	period 	(double): The time period over which the dosage
					 is administered

	Returns the measurement in CPM
	"""
	conversionFactor = 350000 / 1.0
	return conversionFactor * dose / period

trivialCPM 	= convertToCPM(trivialDose, trivialPeriod)
notableCPM 	= convertToCPM(notableDose, notablePeriod)
mediumCPM	= convertToCPM(mediumDose, mediumPeriod)
highCPM 	= convertToCPM(highDose, highPeriod)