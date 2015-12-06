from pathlib import Path


def entity_file_from_path(image_path):
    """Return Entity and File from path"""
    path = Path(image_path)
    entity_name = path.parts[-2]
    file_name = path.stem

    return (entity_name, file_name)
