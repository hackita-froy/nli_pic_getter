import lxml.etree as etree
import suds.client as suds_client
import sys

ENTITY_SEARCH_URL = "http://primo.nli.org.il/PrimoWebServices/xservice/search/brief?institution=NNL_PIC_ALBUM&loc=local,scope:(NNL01_Schwad)&query=any,contains,NNL01_Schwad&sortField=&indx=%s"

# TODO: get all IE's from shvadron as array of strings ['IE1', 'IE2',...,IEn]

