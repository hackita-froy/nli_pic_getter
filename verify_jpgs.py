import logging

import click

from utils import repo

logging.basicConfig(level=logging.INFO)
DEFAULT_PATH = repo.SCHW_ROOT_IMAGE_PATH


@click.command()
@click.option('--path', default=DEFAULT_PATH, help='path to intellectual entity root folder')
def verify_jpgs(path) :
    repo.verify_ie_folders(path)


if __name__ == '__main__':
    verify_jpgs()