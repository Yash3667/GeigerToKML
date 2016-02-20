"""
This script only supports data from a
SAFECAST Geiger Counter. If using other
hardware, script is not guarenteed to work.

Entry point for the program. This
is the script the user will call
along with the parameters
"""

import sys
import getopt
import Parser
#import Mapper
import KMLWriter

def printUsage():
    """
    Print Usage of Script and exits
    """

    print "Converter [OPTION] [FILE]"
    print
    print "Options"
    print
    print "     -i               input file"
    print "     --input          "
    print
    print "     -o               output file"
    print "     --output         "
    print
    print "Examples"
    print
    print "Converter -i LogFile.log -o KMLFile.kml"
    print "Converter -o KMLFile.kml -i LogFile.log"
    exit(0)

""" Script Execution """

logFile = ""
outputFile = ""

# Check for Minimum Arguments
if Parser.checkArguments (sys.argv) == -1:
    print "Error, Not Enough Arguments"
    print
    printUsage ()
else:
    # Get the arguments
    try:
        opts, args = getopt.getopt (sys.argv[1:], "i:o:h", ["input=", "output=", "help"])
    except getopt.GetoptError as err:
        print str(err)
        printUsage ()

# Traverse through the arguments and set values
for option, value in opts:
    if option in ("-h", "--help"):
        printUsage ()
    elif option in ("-i", "--input"):
        logFile = value
    elif option in ("-o", "--output"):
        outputFile = value
    else:
        print "Unknown Error"
        print
        printUsage ()

# Make sure output file has a proper value. Input file will be handled by the Parser
if outputFile == "":
    outputFile = "Untitled.kml"

# Initialize the KML File
KMLWriter.initKML ()

# Get the information from the log file
data = Parser.getInformationFromFile (logFile)
if data == -1:
    print "Parser Couldn't open File Specified"
    exit(1)
elif data == 1:
    print "No Log Data Found in File"
    exit(1)

# Map the data obtained from the log file
Mapper.mapData (data)

# Write all the data to the KML file
KMLWriter.endKML (outputFile)

""" END - Script Execution """
