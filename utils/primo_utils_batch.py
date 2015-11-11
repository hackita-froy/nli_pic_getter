import math
import re
from collections import deque
import os

import lxml.etree as etree
import requests

import models.my_entity as my_entity

entity_list_size = 0
ns = {'primoBib': 'http://www.exlibrisgroup.com/xsd/primo/primo_nm_bib',
        'sears': 'http://www.exlibrisgroup.com/xsd/jaguar/search'}

def get_entities_xml_string(index=1, bulk_size=1000):
    return requests.get(os.environ['ENTITY_SEARCH_URL'].format(index, bulk_size)).content

def get_entity_number():
    tree = get_entity_tree(1,1)
    return int(tree.findall('.//sears:DOCSET', ns)[0].get('TOTALHITS'))


def get_entity_tree(index=1, bulk_size=1000):
    reponse = requests.get(os.environ['ENTITY_SEARCH_URL'].format(index, bulk_size)).content
    return etree.fromstring(reponse)

def create_entity_que(num=get_entity_number()):
    bulk_size = 1000
    intelectual_entities = deque()
    entity_num = num
    iter_num = math.floor(num/bulk_size)
    regex = 'IE[0-9]{1,20}'

    for i in range(0,num):
        tree = get_entity_tree(i*bulk_size+1,bulk_size)
        docs = tree.findall('.//sears:DOCSET/sears:DOC', ns)

        for doc in docs:
            title = doc.find('.//primoBib:title', ns).text
            if re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text) is None:
                print("link {0} could not be retreived".format(doc.find('.//primoBib:linktorsrc', ns).text))
                continue

            ie_id = re.search(regex, doc.find('.//primoBib:linktorsrc', ns).text).group()
            print(ie_id)
            entity = my_entity.MyEntity(ie_id, title)
            intelectual_entities.append(entity)

    return intelectual_entities

