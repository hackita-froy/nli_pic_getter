import logging

import sys

import utils.primo_utils as primo_utils
import utils.repo as repo

def get_entity_files(dest_dir=repo.ZALMANIA_IMAGE_PATH):
    search_url = primo_utils.ZALMANIA_ENTITY_SEARCH_URL
    entity_num = primo_utils.get_entity_number(search_url)
    entities = primo_utils.create_entity_que(search_url, entity_num)
    repo.save_entities_files(entities, dest_dir)
    logging.info("Saving entities")

if __name__ == '__main__':
     # get the path
  try:
    sys.argv[1]
  except IndexError:
    print ("usage: {} path".format(__file__))
    print ("displays number of files and total size of files per extension in the specified path.")
    sys.exit()
  else:
    get_entity_files(sys.argv[1])