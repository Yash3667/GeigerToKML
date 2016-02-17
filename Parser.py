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

    Returns a list on success and -1 on error.

    Parameters
    fileName (String): Path to LOG File
    """

    # Open file in read mode and split content into a List
    try:
        with open (fileName, "r") as logFile:
            fileContent = logFile.read()
    except IOError:
        print "Parser couldn't open file specified"
        return -1
    else:
        fileContent = fileContent.splitlines()

    return fileContent

""" Script Execution """

# Run Forward only if called directly
# Prints all lines in log file beginning with '$'
if __name__ == "__main__":
    check = checkArguments(sys.argv)
    if check:
        print "Error. Not Enough Arguments"
        exit(1)

    fileContent = openFile (sys.argv[1])
    if  fileContent == -1:
        exit(1)
    else:
        for line in fileContent:
            if line[0] == '$':
                print line

""" END - Script Execution """
