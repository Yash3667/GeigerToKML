"""
This is an example script for creating the
simplest Google Earth KML file using the
LXML module for python.

This script is simlpy used to show the usage
of lxml. Everything shown here should be
enough to build any generic xml file.
"""

"""
Module is called lxml
Our main use is from the submodule 'etree'
"""
from lxml import etree as ET

"""
This is how we create tags in lxml

Every Google Earth KML file starts from the kml tag.
Google's documentation lists the xmlns attribute with this website
"""
KMLTag = ET.Element("kml")
KMLTag.set("xmlns", "http://www.opengis.net/kml/2.2")

"""
Notice the use of the method 'SubElement'.
This signifies that this tag is a child under some other tag.
In this case the parent tag is the KML tag
"""
Placemark = ET.SubElement(KMLTag, "Placemark")

PlacemarkName = ET.SubElement(Placemark, "name")
PlacemarkName.text = "Plavemark Name Comes Here" # This is how we set text fields for XML files using lxml etree's

PlacemarkDesc = ET.SubElement(Placemark, "description")
PlacemarkDesc.text = "Placemark Description Comes Here"

PlacemarkPoint = ET.SubElement(Placemark, "Point")
PointCoor = ET.SubElement(PlacemarkPoint, "coordinates") # Notice how coordinates is a child of Point
PointCoor.text = "X, Y, Z" # In KML Files, order: Longitude, Latitude, Altitude

"""
We pass in our root tag. In this case 'KMLTag'

Every Google KML File requires an XML header.
Hence, it is important to set the xml_declaration parameter to True.

Also, KML becomes more universal when using utf-8 encoding, so it
is a good idea to set that as well.

pretty_print is used to signify whether the program should format this
as a traditional XML file or as a single line XML file. I vote traditional!
"""
XML_STR = ET.tostring(KMLTag, encoding = "UTF-8", xml_declaration = True, pretty_print = True)

print
print XML_STR

# Simply writing to a file
with open("TestFile.kml", "w") as File:
    File.write(XML_STR)
