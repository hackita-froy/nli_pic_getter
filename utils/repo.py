import logging
import os
import json
from multiprocessing.pool import Pool

from pathlib import Path
from PIL import Image

from models import my_entity

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

USER_HOME = os.path.expanduser("~")
ROOT_IMAGE_PATH = os.path.join(USER_HOME, "nli_images")
POOL_NUMBER = 10


def save_entities_files(enteties):
    """ Creates and saves IE images in IE folder  """
    pool = Pool(processes=POOL_NUMBER)
    pool.map(save_entity, enteties)

def save_entity(entity):
    """ Creates and saves IE images in IE folder  """
    if entity:
        entity_path = os.path.join(ROOT_IMAGE_PATH, entity.ie_id)
        os.makedirs(entity_path, exist_ok=True)
        entity.save_files(entity_path)


def verify_ie_folders(ie_folder_root_path):
    """ Verifies that all jpgs are valid"""
    ie_folders = Path(ie_folder_root_path)
    corrupt_file_count = 0
    entities = []
    file_ids = []

    try:
        with (ie_folders / "corrupt_file_list.txt").open('w') as f:
            for folder in ie_folders.iterdir():
                if folder.is_file():
                    continue

                for item in folder.iterdir():
                    if item.is_file() and item.suffix == ".jpg":
                        try:
                            img = Image.open(item)
                            img.load()
                            logger.info("{} OK".format(item))
                        except OSError:
                            logger.warn("{} Bad".format(item))
                            file_ids.append(item.stem)
                            logger.info("added {} to file_ids".format(item.stem))
                            f.write("{0}\n".format(item))
                            corrupt_file_count += 1

                if file_ids:
                    entity = my_entity.MyEntity(ie_id=item.parent.stem, file_ids=file_ids)
                    entities.append(entity)
                file_ids = []

    finally:
        if entities:
            print("Fixing corrupt files")
            # save_entities_files(entities)

        entities = []
        print("Number of corrupt files is: {0}".format(corrupt_file_count))

