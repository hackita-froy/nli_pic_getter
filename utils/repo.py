import os
import sys

from pathlib import Path
from PIL import Image

USER_HOME = os.path.expanduser("~")
ROOT_IMAGE_PATH = os.path.join(USER_HOME, "nli_images")

""" Creates and saves IE images in IE folder  """


def save_entities_files(enteties):

    for entity in enteties:
        entity_path = os.path.join(ROOT_IMAGE_PATH, entity.ie_id)
        os.makedirs(entity_path, exist_ok=True)
        entity.save_files(ROOT_IMAGE_PATH)

""" Verifies that all jpgs are valid"""


def verify_ie_folders(ie_folder_root_path):
    ie_folders = Path(ie_folder_root_path)
    corrupt_file_count = 0
    with open("{0}/corrupt_file_list.txt".format(ie_folder_root_path), 'w') as f:
        for folder in ie_folders.iterdir():
            if folder.is_file() and not folder.is_dir():
                next()
            else:
                for item in folder:
                    if item.is_file() and item.suffix == ".jpg" and not item.is_dir():
                        try:
                            image = Image.open(item).load()
                        except IOError:
                            f.write("{0}\n".format(item))
                            corrupt_file_count += 1

        f.write("Number of corrupt files is: {0}".format(corrupt_file_count))
        f.close()





