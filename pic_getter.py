import utils.primo_utils as primo_utils
import utils.repo as repo

if __name__ == '__main__':
    entities = primo_utils.create_entity_que()
    repo.save_enteties_files(entities)