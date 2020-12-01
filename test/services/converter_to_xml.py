from converter import app
import os


def generate_xml_file(xml, filename):
    open(f"{app.config['UPLOAD_FOLDER']}/{filename}.xml", 'w').write(xml)

