import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('../Data/BioMems-XML-example.xml')

# Get the root element
root = tree.getroot()
# It erate over child elements

for child in root:
    print(f"tag: {child.tag}, attribute: {child.attrib}")
    
for x in root[0]:
    print(x.text)
