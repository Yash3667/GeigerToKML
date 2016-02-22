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
import Mapper
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
    print "Converter -i LogFile.log"
    print
    print "If Output File name is not specified, it takes"
    print "on the name of the Log File (the path for the log file is not followed)"
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

# Get the information from the log file
data = Parser.getInformationFromFile (logFile)
if data == -1:
    print "Parser Couldn't open File Specified"
    exit(1)
elif data == 1:
    print "No Log Data Found in File"
    exit(1)

# Make sure output file has a proper value. Input file will be handled by the Parser
if outputFile == "":
    """
    Give it the same name as the logFile

    Also, remove the path (if) trailing
    the logFile by splicing from the last
    occurence from '/'
    """
    outputFile = logFile[logFile.rfind("/") + 1:-4] + ".kml"
elif outputFile[-4:] != ".kml":
    outputFile += ".kml"

print "Logging In:", logFile
print "Outputting:", outputFile

# Initialize the KML File
KMLWriter.initKML ()

# Map the data obtained from the log file
Mapper.mapData (data)

# Write all the data to the KML file
KMLWriter.endKML (outputFile)

""" END - Script Execution """
