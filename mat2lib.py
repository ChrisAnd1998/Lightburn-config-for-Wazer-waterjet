import json
import html

# Read the JSON file
with open('C:/Users/CNC/Desktop/materialdata.json', 'r') as file:
    json_data = file.read()

# Decode the JSON data
data = json.loads(json_data)

# Check if decoding was successful
if data is None:
    print("Error decoding JSON data")
    exit(1)

xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_string += '<LightBurnLibrary>\n'

# Iterate over each entry and construct the XML
for entry in data:
    for rate_type in [('speedRoughRate', 'Rough'), 
                      ('speedMediumRate', 'Medium'), 
                      ('speedFineRate', 'Fine')]:
        
        speed_rate_key, speed_desc = rate_type
        speed_rate = entry[speed_rate_key]
        
        xml_string += f'  <Material name="{entry["name"]}">\n'
        xml_string += f'    <Entry Thickness="-1.0000" Desc="Spd: {speed_rate} ({speed_desc}) Pce: {entry["pierceTime"]}" NoThickTitle="{entry["thickness"]}">\n'
        xml_string += f'      <CutSetting type="Cut">\n'
        xml_string += '        <index Value="0"/>\n'
        xml_string += '        <name Value=""/>\n'
        xml_string += f'        <LinkPath Value="{entry["name"]}/{entry["thickness"]}/{entry["category"].replace("&", "and")}"/>\n'
        xml_string += '        <minPower Value="4"/>\n'
        xml_string += '        <maxPower Value="100"/>\n'
        xml_string += '        <maxPower2 Value="20"/>\n'
        xml_string += f'        <speed Value="{float(speed_rate.replace("in/min", "").replace("mm/min", "")) / 60}"/>\n'
        xml_string += f'        <startDelay Value="{entry["pierceTime"].replace("s", "")}"/>\n'
        xml_string += '        <leadIn Value="1"/>\n'
        xml_string += '        <leadLength Value="5"/>\n'
        xml_string += '        <leadAngle Value="90"/>\n'
        xml_string += '        <leadStyle Value="arc"/>\n'
        xml_string += '        <priority Value="0"/>\n'
        xml_string += '        <tabCount Value="1"/>\n'
        xml_string += '        <tabCountMax Value="1"/>\n'
        xml_string += '      </CutSetting>\n'
        xml_string += '    </Entry>\n'
        xml_string += '  </Material>\n'

# End the XML string
xml_string += '</LightBurnLibrary>\n'

# Write the XML string to a file
with open(r'C:\Users\CNC\Desktop\WAZER Library.clb', 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_string)

print("XML data has been exported to materialdata.xml")