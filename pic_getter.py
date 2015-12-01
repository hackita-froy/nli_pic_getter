import logging

import utils.primo_utils as primo_utils
import utils.repo as repo

if __name__ == '__main__':
    entities = primo_utils.create_entity_que()
    repo.save_entities_files(entities, repo.SCHW_ROOT_IMAGE_PATH)
    logging.info("Saving entities")
