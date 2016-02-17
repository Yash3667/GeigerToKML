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

def openFile (fileName):
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
    [4]: Latitude in ddmm.mmmm (dd -> degrees; mm.mmmm -> minutes)
    [5]: Hemisphere for Latitude
    [6]: Longitude in dddmm.mmmm (ddd -> degrees; mm.mmmm -> minutes)
    [7]: Hemisphere for Londitude
    [8]: Altitude
    [9]: GPS Location Validity Flag
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

        for line in fileContent:
            if line[0] == '$':
                fileList.append(line.split(","))

        for i in range (len (fileList)):
            fileList[i] = fileList[i][3:-2]

    return fileList

""" Script Execution """

# Run Forward only if called directly
# Prints all lines in log file beginning with '$'
if __name__ == "__main__":
    check = checkArguments(sys.argv)
    if check:
        print "Error. Not Enough Arguments"
        exit(1)

    fileList = openFile (sys.argv[1])
    if  fileList == -1:
        exit(1)
    else:
        for line in fileList:
                print line

""" END - Script Execution """
