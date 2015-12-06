import os
import random
import sys
from pathlib import Path
from pip.utils import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
"""
goes over the directory and checks whether images are portraits
"""


def save_portrait_to_db(image_path):
    path = Path(image_path)



def clasify_files(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            if is_portrait(os.path.join(root, name)):
                save_portrait_to_db(os.path.join(root, name))
                logger("Portrait! %" % os.path.join(root, name))

        # for name in dirs:
        #     print(os.path.join(root, name))

def is_portrait(image_path):
    # add image formats as needed
    if image_path.endswith(('.jpg', '.png', '.tif')):
        ## TODO: implement face detection
        return bool(random.getrandbits(1))
    return False