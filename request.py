import requests
import aiohttp
import asyncio
import base64
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from lxml import etree as ET
from xml.dom import minidom
from xmlparser import Find_result_set

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
      
def CallCPI( address, name, passw, operation, direction, number,taxId, checkId, dateFrom, dateTo, page, transactionId ):

    AuthData = name + ':' + passw
    base64Data = (base64.b64encode(AuthData.encode("utf-8"))).decode('utf-8')
    headers = {}
    headers['Content-Type'] = 'text/html;charset=utf-8'
    headers['Authorization'] = 'Basic ' + str(base64Data)
    body = buildBody(operation, direction, number, checkId, taxId, dateFrom, dateTo, page, transactionId)

    try:
        response = requests.post(address, data = body,  headers=headers)
        if (response.content).decode('utf-8') == '':
            return 'failed to call CPI. Please go to the main page and try to Ping tenant '
        else:  
            return((response.content).decode('utf-8'))
        
    except:
        return 'failed to call CPI. Please go to the main page and try to Ping tenant '

async def CallCPI_Async( address, name, passw, operation, direction, number,taxId, checkId, dateFrom, dateTo, page, pages, transactionId, transactions ):

    AuthData = name + ':' + passw
    base64Data = (base64.b64encode(AuthData.encode("utf-8"))).decode('utf-8')
    headers = {}
    headers['Content-Type'] = 'text/html;charset=utf-8'
    headers['Authorization'] = 'Basic ' + str(base64Data)
    tasks = []
    
    try:
        if transactions != '':
            
            for transaction in transactions:
                body = buildBody(operation, direction, number, checkId, taxId, dateFrom, dateTo, str(page), transaction[1]) 
                task = asyncio.ensure_future(post(address, body, headers, transaction = transaction[1], line = transaction[0]))
                tasks.append(task)
            responses = asyncio.gather(*tasks)
            await responses    
            return responses._result
        else:  
            for page in range(int(page), int(pages) + 1):
                body = buildBody(operation, direction, number, checkId, taxId, dateFrom, dateTo, str(page), transactionId)
                task = asyncio.ensure_future(post(address, body, headers))
                tasks.append(task)
            responses = asyncio.gather(*tasks)
            await responses    
            return responses._result
    except:
        return 'failed to call CPI. Please go to the main page and try to Ping tenant '

async def post(address, body, headers, *args, **kwargs):   
     result_set = {} 
     transaction = kwargs.get('transaction', None)
     line = kwargs.get('line', None)
     async with aiohttp.ClientSession() as session:
              async with session.post(address, data = body, headers = headers) as response:
                if transaction != None:
                    returning = []
                    returning.append(line)
                    returning.append(transaction)
                    returning.append((response.content._buffer[0]).decode('utf-8'))
                    response = returning
                else:
                    response = (response.content._buffer[0]).decode('utf-8')  
                try:
                    result_set = Find_result_set(response)
                except:       
                    result_set = {}  
                    # make  extra call in case if iflow failed                   
                if result_set.get('ErrorText') != None or result_set == {}:  
                    try:
                        response2 = requests.post(address, data = body,  headers=headers) 
                        if transaction != None:
                            returning = []
                            returning.append(line)
                            returning.append(transaction)
                            returning.append((response2.content).decode('utf-8'))
                            response2 = returning
                        else:
                            response2 = (response2.content).decode('utf-8')   
                        return response2
                    except:    
                        return response
                else:
                    return response          
                
def buildBody(operation, direction, number, checkId, taxId, dateFrom, dateTo, page, transactionId):
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
    child10 = ET.SubElement(top, 'Direction')
    child10.text = direction
    child11 = ET.SubElement(top, 'DateFrom')
    child11.text = dateFrom
    child12 = ET.SubElement(top, 'DateTo')
    child12.text = dateTo
    child13 = ET.SubElement(top, 'Page')
    child13.text = page
    child14 = ET.SubElement(top, 'TransactionId')
    child14.text = transactionId
    return((ET.tostring(env).decode('utf-8')))