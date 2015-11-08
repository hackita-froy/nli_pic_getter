import sys
import os

import lxml.etree as etree
import suds
import suds.client as suds_client


ROSETTA_WSDL_URL = os.environ['ROSETTA_WSDL_URL']
FILE_ID_ATTR = 'FILEID'


def get_rosetta_client():
    return suds_client.Client(ROSETTA_WSDL_URL)

def get_rosetta_delivery_service():
    return get_rosetta_client().service

def get_entity_file_ids(ie_id):
    ns = {'mets': 'http://www.loc.gov/METS/'}
    fl_list = []
    try:
        result = get_rosetta_delivery_service().getIE(ie_id)
    except suds.WebFault as e :
        print('an web error happend, entity not retrieved')
        print(e)

    tree = etree.fromstring(result)
    fptr_elements = tree.findall('.//mets:structMap[1]//mets:fptr', ns)
    for element in fptr_elements:
        fl_list.append(element.get(FILE_ID_ATTR))

    return fl_list




if __name__ == '__main__':
    ie_id = ''
    file_ids = []
    if len(sys.argv) > 1:
        ie_id = sys.argv[1]
        if isinstance(ie_id, str):
           file_ids =  get_entity_file_ids(ie_id)
    else:
        sys.exit("you must supply an IE ID as the first argument")

    print(file_ids)




