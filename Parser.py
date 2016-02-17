"""
Module for parsing SAFECAST Geiger Counter LOG Files
into a Python List.

Returning -1 represents error.
"""

import sys

def checkArguments (arguments):
    """
    Checks for the minimum # of arguments.
    Returns 0 on success and -1 on failure.

    Parameters
    arguments (String): Command line parameters passed by user
    """
    # Minimum Argument Count: 2
    if (len (arguments) >= 2):
        return 0
    else:
        return -1

def getInformationFromFile (fileName):
    """
    Tries to open file in read mode
    and gets a list of all the different
    lines in the LOG file.

    Returns a multi-dimensional list on success and -1 on error.

    Parameters
    fileName (String): Path to LOG File

    Attributes for the returned list
    [0]: Radiation in the last minute
    [1]: Radiation in the last five seconds
    [2]: Radiation total count since start up
    [3]: Radiation Count Validity Flag
    [4]: Longitude in Decimal Notation
    [5]: Latitude in Decimal Notation
    [6]: Altitude
    [7]: GPS Location Validity Flag
    """

    fileList = []
    # Open file in read mode and split content into a List
    try:
        with open (fileName, "r") as logFile:
            fileContent = logFile.read()
    except IOError:
        print "Parser couldn't open file specified"
        return -1
    else:
        fileContent = fileContent.splitlines()

        # Get only relevant lines and split into serparate token from the LOG file
        for line in fileContent:
            if line[0] == '$':
                fileList.append(line.split(","))

        # Remove unwanted tokens from each line
        for i in range (len (fileList)):
            fileList[i] = fileList[i][3:-2]

            # Get Decimal Latitude and Longitude
            """
            The LOG file gives these notations. These need to be changed
            to decimal notation.

            Google KML needs longitude first, so it makes more sense to
            place it earlier in the list rather than later.
            """
            longitude = convertToDecimal(fileList[i][6], fileList[i][7]) # Longitude is the 7th Element and its Hemisphere is the 8th
            latitude  = convertToDecimal(fileList[i][4], fileList[i][5]) # Latitude is the 5th Element and its Hemisphere is the 6th

            # Change Values in List and remove Hemisphere Orientation
            fileList[i][4] = str(longitude)
            fileList[i][6] = str(latitude)
            del fileList[i][5]
            del fileList[i][6] # Remove 6 and not 7 because there is one less element now

    return fileList

def convertToDecimal(point, hemisphere):
    """
    Take a latitude or longitude in LOG File
    notation and return a decimal notation
    depending on the hemisphere

    Formula
    Decimal = Degree + (Minutes / 60)

    Parameters
    point      (String): Point Notation according to log
    hemisphere (String): Hemisphere orientation for point
    """

    # Orientation is negative for W and S and positive for N and E
    orientation = 1

    if hemisphere in ("N", "S"):
        degree = int(point[0:2])
        minute = float(point[2:])

        # Set Orientation
        if hemisphere == "S":
            orientation = -1
    elif hemisphere in ("E", "W"):
        degree = int(point[0:3])
        minute = float(point[3:])

        # Set Orientation
        if hemisphere == "W":
            orientation = -1

    # Apply Formula
    decimal = (degree + (minute / 60)) * orientation

    return decimal

""" Script Execution """

# Run Forward only if called directly
# Prints all lines
if __name__ == "__main__":
    check = checkArguments(sys.argv)
    if check:
        print "Error. Not Enough Arguments"
        exit(1)

    fileList = getInformationFromFile (sys.argv[1])
    if  fileList == -1:
        exit(1)
    else:
        for line in fileList:
                print line

""" END - Script Execution """
