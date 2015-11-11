import os
import urllib.request

USER_HOME = os.path.expanduser("~")
ROOT_IMAGE_PATH = os.path.join(USER_HOME, "nli_images")

""" Creates and saves IE images in IE folder  """
def save_enteties_files(enteties):

    for entity in enteties:
        entity_path = os.path.join(ROOT_IMAGE_PATH, entity.ie_id)
        os.makedirs(entity_path, exist_ok=True)
        entity.save_files(ROOT_IMAGE_PATH)