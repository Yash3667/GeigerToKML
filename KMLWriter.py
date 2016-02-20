def initKML():
  global ET
  global KMLTag
  from lxml import etree as ET
  KMLTag = ET.Element("kml")
  KMLTag.set("xmlns", "http://www.opengis.net/kml/2.2")



def makeLine(points,color,look=False):
  Document = ET.SubElement(KMLTag,"Document")
  Style = ET.SubElement(Document, "Style", id=color)
  Placemark = ET.SubElement(Document, "Placemark")
  LineStyle = ET.SubElement(Style,"LineStyle")
  colorTag = ET.SubElement(LineStyle,"color")
  colorTag.text = color
  widthTag = ET.SubElement(LineStyle,"width")
  widthTag.text = "2"
  styleUrl = ET.SubElement(Placemark,"styleUrl")
  styleUrl.text = "#"+color
  LineString = ET.SubElement(Placemark, "LineString")
  LineStringTess = ET.SubElement(LineString, "tessellate")
  LineStringTess.text = "1"
  LineStringCoor = ET.SubElement(LineString, "coordinates")
  LineStringCoor.text = ""
  for point in points:
    coor = str(point[0])+","+str(point[1])+","+"0\n"
    LineStringCoor.text = LineStringCoor.text+coor
    print(coor)


def endKML(fileName):
  XML_STR = ET.tostring(KMLTag, encoding = "UTF-8", xml_declaration = True, pretty_print = True)
  with open(fileName, "w") as File:
      File.write(XML_STR)


initKML()
makeLine([[100, 59], [100, 50.00394857394857]], "7f0000ff")
endKML("TestFile")


