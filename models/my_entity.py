import urllib
import logging
import os

import utils.rosetta_utils as rosetta_utils

logger = logging.getLogger(__name__)

class MyEntity:
    def __init__(self, ie_id, title):
        self.ie_id = ie_id
        self.title = title
        self.files_ids = self.get_files_ids()

    def get_files_ids(self):
        return rosetta_utils.get_entity_file_ids(self.ie_id)

    def save_files(self, path):
        for file in self.files_ids:
            file_path = path + "/{0}.jpg".format(file)
            urllib.request.urlretrieve(os.environ['ROSETTA_FILE_RETRIEVE']
                                       .format(file), file_path)
            logger.info("wrote {0}".format(file_path))
            with open(path+"/title.text", "w") as text_file:
                text_file.write(self.title)
