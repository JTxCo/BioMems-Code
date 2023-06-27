import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('../Data/BioMems-XML-example.xml')

# Get the root element
root = tree.getroot()
# It erate over child elements
sampleData = root.find('./sampleData')
well = sampleData.find('./well1Data')
# for well in sampleData.findall('*'):
if well is not None:
    print(well.tag)
    print('  Well Data:', well.text)
    
    info = well.find('./info')
    print('  Info:')
    for data in info.findall('*'):
        print('    ', data.tag, data.text)
        
    samples = well.findall('./sample/*')
    print('  Samples:')
    for sample in samples:
        print('    ', sample.tag, sample.text)
        
    print('\n')
    print()

    
    
    


