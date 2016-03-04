"""
These variables are tunable parameters that control when
milestone colors are reached (see documentation for further 
details). 
"""

trivialDose 	= 3
trivialPeriod	= 24 * 365

mediumDose		= 130
mediumPeriod	= 24 * 365

highDose		= 700
highPeriod	= 24 * 365

veryHighDose		= 170
veryHighPeriod		= 24 * 7



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
mediumCPM 	= convertToCPM(mediumDose, mediumPeriod)
highCPM 	= convertToCPM(highDose, highPeriod)
veryHighCPM = convertToCPM(veryHighDose, veryHighPeriod)