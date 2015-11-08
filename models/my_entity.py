import utils.rosetta_utils as rosetta_utils
class MyEntity:
    ie_id = ''
    title = ''
    files_ids = []

    def __init__(self, ie_id, title):
        self.ie_id = ie_id
        self.title = title
        self.files_ids = get_files_ids()


def get_files_ids(self):
    return rosetta_utils.get_entity_file_ids(self.ie_id)