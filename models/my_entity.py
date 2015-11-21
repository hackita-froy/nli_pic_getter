import urllib
import logging
import os

from pathlib import Path

import utils.rosetta_utils as rosetta_utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyEntity(object):
    def __init__(self, ie_id, file_ids=None, title=''):
        self.ie_id = ie_id
        self.title = title
        if not file_ids:
            self.files_ids = self.get_files_ids()
        else:
            self.files_ids = file_ids

    def get_files_ids(self):
        return rosetta_utils.get_entity_file_ids(self.ie_id)

    def save_files(self, path):
        if self.files_ids:
            for file in self.files_ids:
                file_path = path + "/{0}.jpg".format(file)
                urllib.request.urlretrieve(os.environ['ROSETTA_FILE_RETRIEVE']
                                           .format(file), file_path)
                logger.info("wrote {0}".format(file_path))
                if not Path(path+"/title.text").is_file():
                    with open(path+"/title.text", "w") as text_file:
                        text_file.write(self.title)
