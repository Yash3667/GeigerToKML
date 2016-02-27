"""
Module for writing paths to a KML file.
"""

def initKML(widthLength = "10"):
    """
    Initializes KML tree and makes the
    """
    global ET
    global KMLTag
    global Document
    global widthText

    widthText = widthLength

    from lxml import etree as ET

    KMLTag = ET.Element("kml")
    KMLTag.set("xmlns", "http://www.opengis.net/kml/2.2")
    Document = ET.SubElement(KMLTag,"Document")



def makeLine(points,color,radLevel):
    """
    This is the main function of the module

    Parameters
    points      (list): a list of length 7 lists
                        who's elements are detailed in Parser.py
    color     (string): a abgr hex code
    radLevel  (string): the radiation level for the path as a string
    """
    #this creates the style tag that will give the LineString it's color and width
    Style = ET.SubElement(Document, "Style", id=color)
    LineStyle = ET.SubElement(Style,"LineStyle")
    colorTag = ET.SubElement(LineStyle,"color")
    colorTag.text = color
    widthTag = ET.SubElement(LineStyle,"width")
    widthTag.text = widthText

    #This creates the Placemark that will cointain the LineString
    Placemark = ET.SubElement(Document, "Placemark")
    #This links up the Placemark and the style tag
    styleUrl = ET.SubElement(Placemark,"styleUrl")
    styleUrl.text = "#"+color
    name = ET.SubElement(Placemark,"name")
    name.text = radLevel+"cpm"
    description = ET.SubElement(Placemark,"description")
    description.text = str(points[1][0]).replace("T"," ").replace("Z","")

    #This creates the LineString, tessellates it, and initializes the coordinates tag
    LineString = ET.SubElement(Placemark, "LineString")
    LineStringTess = ET.SubElement(LineString, "tessellate")
    LineStringTess.text = "1"
    LineStringCoor = ET.SubElement(LineString, "coordinates")
    LineStringCoor.text = ""
    for point in points:
        #for each point on the line add it's cordinates to the cordinate tag
        coor = str(point[5])+","+str(point[6])+","+str(point[7])+"\n"
        LineStringCoor.text = LineStringCoor.text+coor


def endKML(fileName):
    """
    Closes KML tree and writes it to a file
    Parameters
    fileName (string): the file you would like to write to
                       ex: example.kml
    """
    XML_STR = ET.tostring(KMLTag, encoding = "UTF-8", xml_declaration = True, pretty_print = True)
    with open(fileName, "w") as File:
      File.write(XML_STR)



if __name__ == "__main__":
    initKML()
    makeLine([[-112.0814237830345,36.10677870477137],[-112.0870267752693,36.0905099328766], [-112.0880267752693,36]], "7f0000ff")
    endKML("TestFile.kml")
