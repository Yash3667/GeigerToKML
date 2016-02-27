"""
Module for parsing SAFECAST Geiger Counter LOG Files
into a Python List.

Returning -1 represents IOError
Returning  1 represents Data Error
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

    Element Index's for the returned list
    [0]: Time Stamp in UTC
    [1]: Radiation in the last minute
    [2]: Radiation in the last five seconds
    [3]: Radiation total count since start up
    [4]: Radiation Count Validity Flag
    [5]: Longitude in Decimal Notation
    [6]: Latitude in Decimal Notation
    [7]: Altitude
    [8]: GPS Location Validity Flag
    """

    fileList = []
    # Open file in read mode and split content into a List
    try:
        with open (fileName, "r") as logFile:
            fileContent = logFile.read()
    except IOError:
        return -1
    else:
        fileContent = fileContent.splitlines()

        if len(fileContent) == 0:
            return 1
        else:
            """
            print fileContent
            print
            """

        # Get only relevant lines and split into serparate token from the LOG file
        for line in fileContent:
            #print line
            if len(line):
                if line[0] == '$': # Makes sure only LOG files are used
                    fileList.append(line.split(","))

        # Check for zero number of lines
        if len (fileList) == 0:
            return 1

        # Remove unwanted tokens from each line
        for i in range (len (fileList)):
            fileList[i] = fileList[i][2:-2]

            # Get Decimal Latitude and Longitude
            """
            The LOG file gives these notations. These need to be changed
            to decimal notation.

            Google KML needs longitude first, so it makes more sense to
            place it earlier in the list rather than later.
            """
            longitude = convertToDecimal (fileList[i][7], fileList[i][8]) # Longitude is the 8th Element and its Hemisphere is the 9th
            latitude  = convertToDecimal (fileList[i][5], fileList[i][6]) # Latitude is the 6th Element and its Hemisphere is the 7th

            # Change Values in List and remove Hemisphere Orientation
            fileList[i][5] = str (longitude)
            fileList[i][7] = str (latitude)

            del fileList[i][6]
            del fileList[i][7] # Remove 7 and not 8 because there is one less element now

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
        degree = int (point[0:2])
        minute = float (point[2:])

        # Set Orientation
        if hemisphere == "S":
            orientation = -1
    elif hemisphere in ("E", "W"):
        degree = int (point[0:3])
        minute = float (point[3:])

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
    check = checkArguments (sys.argv)
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
