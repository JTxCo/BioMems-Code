import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('../Data/BioMems-XML-example.xml')

# Get the root element
root = tree.getroot()
# It erate over child elements
sampleData = root.find('./sampleData')
for well in sampleData.findall('*'):
    print(well.tag)
    print('  Well Data:', well.text)
    
    info = well.find('./info')
    print('  Info:')
    for data in info.findall('*'):
        print('    ', data.tag, data.text)
        
    samples = well.find('./sample')
    print('  Samples:')
    for data in samples.findall('*'):
        print('    ', data.tag, data.text)
        
    print()

    
    
    


