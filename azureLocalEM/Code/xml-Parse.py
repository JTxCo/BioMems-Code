import xml.etree.ElementTree as ET

tree = ET.parse('./Data/BioMems-XMLTEST.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)