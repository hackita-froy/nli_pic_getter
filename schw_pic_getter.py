import logging

import sys

import utils.primo_utils as primo_utils
import utils.repo as repo

def main(dest_dir=repo.SCHW_ROOT_IMAGE_PATH):
    entities = primo_utils.create_entity_que()
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
    main(sys.argv[1])
