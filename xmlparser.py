import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from lxml import etree

def Find_result_set(xml):
    try:
        root = etree.fromstring(xml)
    except:
        pass
    # Remove namespace prefixes
    for elem in root.getiterator():
        elem.tag = etree.QName(elem).localname
    # Remove unused namespace declarations
    etree.cleanup_namespaces(root)
    # Parse xml
    tree = ET.fromstring(etree.tostring(root).decode())
    # find tag content
    result_set = {}
    for elem in tree.iter():
       if elem.text != None :
           result_set[elem.tag] = elem.text
    return result_set