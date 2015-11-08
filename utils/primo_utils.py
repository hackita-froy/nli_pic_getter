import sys
import os
import re
from collections import deque

import lxml.etree as etree
import requests

import models.my_entity as my_entity

ENTITY_SEARCH_URL = os.environ['ENTITY_SEARCH_URL']


entity_list_size = 0
ns = {'primoBib': 'http://www.exlibrisgroup.com/xsd/primo/primo_nm_bib',
        'sears': 'http://www.exlibrisgroup.com/xsd/jaguar/search'}

""" Return the xml string response from primo search query"""
def get_entities_xml_string(index=1):
    return requests.get(ENTITY_SEARCH_URL.format(index)).content

""" Return the number of results from primo search query """
def get_entity_number():
    tree = get_entity_tree()
    return int(tree.findall('.//sears:DOCSET', ns)[0].get('TOTALHITS'))

""" Return lxml.etree tree representing the xml response from primo """
def get_entity_tree(index=1):
    reponse = requests.get(ENTITY_SEARCH_URL % index).content
    return etree.fromstring(reponse)

""" Return a dque of model.my_entity.MyEntity of all Schwadron IEs """
def create_entity_que(num=get_entity_number()):
    intelectual_entities = deque()
    entity_num = num
    regex = 'IE[0-9]{1,20}'

    for i in range(1, num):
        global ns
        tree = get_entity_tree(i)
        doc = tree.findall('.//sears:DOCSET/sears:DOC', ns)[0]
        title = doc.find('.//primoBib:title', ns).text

        if re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text) is None:

            continue

        ie_id = re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text).group()
        print("initializing {0}".format(ie_id))
        entity = my_entity.MyEntity(ie_id, title)
        intelectual_entities .append(entity)

    return intelectual_entities



# TODO: get all IE's from shvadron as array of strings ['IE1', 'IE2',...,IEn]

