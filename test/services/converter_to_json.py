import json
import xmltodict
from converter.util.operations_file import process_xml_file
from converter import app
import xml.etree.ElementTree as ET


def generate_json_file(xml, filename):
    # import ipdb; ipdb.set_trace()
    # xml_data = ET.fromstring(xml)
    json_data = json.dumps(xmltodict.parse(xml), indent=4)
    open(f"{app.config['UPLOAD_FOLDER']}/{filename}.json", 'w').write(json_data)
