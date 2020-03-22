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
    # find tags content and put to dictionary
    result_set = {}
    for elem in tree.iter():
       if elem.text != None :
           result_set[elem.tag] = elem.text
    return result_set
  
def Find_Element_value(xml, name):
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
    result = ''
    for elem in tree.iter():
       if elem.text != None and elem.tag == name :
           result = elem.text
    return result
  
def Parse_Transaction_List(xml, result_set):
  # this method parse xml and add transaction found lines to result_set
    try:
        root = etree.fromstring(xml)
    except:
        pass
 
    for elem in root.getiterator():
        elem.tag = etree.QName(elem).localname
        etree.cleanup_namespaces(root)
        tree = ET.fromstring(etree.tostring(root).decode())
        temp_set = {}
    
    for elem in tree.iter():
        if elem.tag == 'transaction' :
            temp_set = {}
            for child in elem:
                temp_set[child.tag]  = child.text
            result_set.append(temp_set)
           
  
    return result_set