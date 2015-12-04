import logging
import sys
import os
import re
import pdb
from collections import deque
from functools import partial
from multiprocessing.pool import Pool

import lxml.etree as etree
import requests

import models.my_entity as my_entity

ENTITY_SEARCH_URL = os.environ['ENTITY_SEARCH_URL']
ZALMANIA_ENTITY_SEARCH_URL = os.environ['ZALMANIA_ENTITY_SEARCH_URL']

POOL_NUMBER = 10

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


entity_list_size = 0
ns = {'primoBib': 'http://www.exlibrisgroup.com/xsd/primo/primo_nm_bib',
        'sears': 'http://www.exlibrisgroup.com/xsd/jaguar/search'}

""" Return the xml string response from primo search query"""
def get_entities_xml_string(index=1):
    return requests.get(ENTITY_SEARCH_URL.format(index)).content

""" Return the number of results from primo search query """
def get_entity_number(search_url):
    tree = get_entity_tree(search_url)
    return int(tree.findall('.//sears:DOCSET', ns)[0].get('TOTALHITS'))

""" Return lxml.etree tree representing the xml response from primo """
def get_entity_tree(search_url, index=1):
    try:
        logger.info("getting entity tree from {}".format(search_url))
        reponse = requests.get(search_url.format(index, 1)).content
        return etree.fromstring(reponse)
    except ConnectionError as e :
        logger.error(e)


""" Return a dque of model.my_entity.MyEntity of all Schwadron IEs """
def create_entity_que(search_url, num=1):
    intelectual_entities = deque()
    regex = 'IE[0-9]{1,20}'
    print("num = %i" % num)
    for i in range(1, num): # TODO: test loop might be loosing one ent
        global ns
        tree = get_entity_tree(search_url, i)
        doc = tree.findall('.//sears:DOCSET/sears:DOC', ns)[0]
        title = doc.find('.//primoBib:title', ns).text

        if re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text) is None:

            continue

        ie_id = re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text).group()
        print("initializing {0}".format(ie_id))
        entity = my_entity.MyEntity(ie_id=ie_id, title=title)
        intelectual_entities .append(entity)

    return intelectual_entities



""" Return a dque of model.my_entity.MyEntity of all Schwadron IEs """
def get_entity(search_url, index=1):
    assert search_url
    regex = 'IE[0-9]{1,20}'

    global ns
    tree = get_entity_tree(search_url, index)
    doc = tree.findall('.//sears:DOCSET/sears:DOC', ns)[0]
    title = doc.find('.//primoBib:title', ns).text

    if re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text) is None:

        return

    ie_id = re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text).group()
    entity = my_entity.MyEntity(ie_id=ie_id, title=title)
    logger.info("initialized {0}".format(ie_id))

    return entity
