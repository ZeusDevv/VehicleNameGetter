import xml.etree.ElementTree as ET
import json

def parse_vehicles_meta(file_path):
    data = []

    tree = ET.parse(file_path)
    root = tree.getroot()

    for item in root.findall('.//Item'):
        modelname_element = item.find('modelName')
        if modelname_element is not None and modelname_element.text:
            modelname = modelname_element.text
            data.append(f'{modelname}')

    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)


file_path = 'path/to/vehicles.meta'
output_file = 'output.json'

parsed_data = parse_vehicles_meta(file_path)
save_to_json(parsed_data, output_file)
