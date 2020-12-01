from zipfile import ZipFile
from converter import app
from werkzeug.utils import secure_filename
from converter.services.converter_to_xml import generate_xml_file
import os


def save_local_file(file):
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    return filename.split('.')[0]


def remove_files(func):
    def wrapper():
        result = func()
        files_names = os.listdir(app.config['UPLOAD_FOLDER'])
        [os.remove(f'{app.config["UPLOAD_FOLDER"]}/{name}') for name in files_names]
        return result
    return wrapper


def process_xml_file(func):
    def wrapper(filename):
        generate_xml_file(filename)
        result = func(filename)
        return result
    return wrapper


def zip_files(zipname, *filenames):
    zipObj = ZipFile(f"{app.config['UPLOAD_FOLDER']}/{zipname}.zip", 'w')
    for filename in filenames:
        zipObj.write(f"{app.config['UPLOAD_FOLDER']}/{filename}", f"{filename}")
    zipObj.close()