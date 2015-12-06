import logging
import os
import random
import sys
from pathlib import Path

from utils import repo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clasify_files(root_dir):

    """Clasify files in a given directory to prortrait or not.

    Traverses all sub directories of the given root
    Saves to db if portrait
    """
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            is_port = is_portrait(os.path.join(root, name))
            if is_port[0]:
                repo.save_portrait_to_db(os.path.join(root, name), is_port[1])
                logger.info("Portrait! %s" % os.path.join(root, name))
            logger.error("NOT Portrait! %s" % os.path.join(root, name))


        # for name in dirs:
        #     print(os.path.join(root, name))

def is_portrait(image_path):
    """Return a tuple (is_portrait, portrait_bounding_box)"""

    # add image formats as needed
    if image_path.endswith(('.jpg', '.png', '.tif')):
        ## TODO: implement face detection
        is_port = bool(random.getrandbits(1))
        if is_port:# tHIS IS A PLACE HOLDER FOR THE REAL FUNC
            return (is_port, rand_face_location_tuple())

    return (False, None)

def rand_face_location_tuple():
    x1 = random.randint(0,600)
    x2 = random.randint(0,600)
    y1 = random.randint(0,600)
    y2 = random.randint(0,600)
    return (x1,y1,x2,y2)