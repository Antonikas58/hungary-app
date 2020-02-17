import requests
import base64


def Ping( address, name, passw):

    AuthData = name + ':' + passw
    base64Data = (base64.b64encode(AuthData.encode("utf-8"))).decode('utf-8')
    headers = {}
    headers['Content-Type'] = 'text/html;charset=utf-8'
    headers['Authorization'] = 'Basic ' + str(base64Data)
    response = requests.post(address, headers=headers)
    if response.status_code == 500:
        return True
    else:
        return False
