import requests
import base64
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from lxml import etree as ET
from xml.dom import minidom

def Ping( address, name, passw):

    AuthData = name + ':' + passw
    base64Data = (base64.b64encode(AuthData.encode("utf-8"))).decode('utf-8')
    headers = {}
    headers['Content-Type'] = 'text/html;charset=utf-8'
    headers['Authorization'] = 'Basic ' + str(base64Data)
    try:
        response = requests.post(address, headers=headers)
        if response.status_code == 500:
            return True
        else:
            return False
    except:
        return False  
      
def CallCPI( address, name, passw, operation, direction, number,taxId, checkId ):

    AuthData = name + ':' + passw
    base64Data = (base64.b64encode(AuthData.encode("utf-8"))).decode('utf-8')
    headers = {}
    headers['Content-Type'] = 'text/html;charset=utf-8'
    headers['Authorization'] = 'Basic ' + str(base64Data)
    body = buildBody(operation, direction, number, checkId, taxId)

    try:
        response = requests.post(address, data = body,  headers=headers)
        return((response.content).decode('utf-8'))
   
    except:
        return 'failed to call CPI. Please go to the main page and try to Ping tenant '
def buildBody(operation, direction, number, checkId, taxId):
    SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
    ns_map = {'soap-env': SOAP_NS}  
    ET.register_namespace('soap-env',"http://schemas.xmlsoap.org/soap/envelope/") 
    env = ET.Element(ET.QName(SOAP_NS, 'Envelope'), nsmap=ns_map)
    head = ET.SubElement(env, ET.QName(SOAP_NS, 'Header'), nsmap=ns_map)
    body = ET.SubElement(env, ET.QName(SOAP_NS, 'Body'), nsmap=ns_map)
    top = ET.SubElement(body,'ManageInvoiceRequest')
    
    child = ET.SubElement(top, 'SoftwareID')
    child.text = 'SAP-S4HANA-1909-OP'
    child1 = ET.SubElement(top, 'SoftwareName')
    child1.text = 'SAP'
    child2 = ET.SubElement(top, 'SoftwareOperation')
    child2.text = 'LOCAL_SOFTWARE'
    child3 = ET.SubElement(top, 'SoftwareMainVersion')
    child3.text = 'SAP SE'
    child4 = ET.SubElement(top, 'SoftwareDevName')
    child4.text = 'info@sap.com'
    child5 = ET.SubElement(top, 'SoftwareDevContact')
    child5.text = 'SAP-S4HANA-1909-OP'
    child6 = ET.SubElement(top, 'TaxpayerId')
    child6.text = taxId
    child7 = ET.SubElement(top, 'CheckId')
    child7.text = checkId
    child8 = ET.SubElement(top, 'InvoiceNumber')
    child8.text = number
    child9 = ET.SubElement(top, 'WebOperation')
    child9.text = operation
    child0 = ET.SubElement(top, 'Direction')
    child0.text = direction

    return((ET.tostring(env).decode('utf-8')))
    