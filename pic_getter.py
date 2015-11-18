import utils.primo_utils_batch as primo_utils
import utils.repo as repo

if __name__ == '__main__':
    entities = primo_utils.create_entity_que()
    repo.save_entities_files(entities)