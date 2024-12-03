from ServiceRequestData import ServiceRequestList
import requests
from getToken import generateToken
import json

#print(ServiceRequestList())

lista = ServiceRequestList()
urlIFS_token = generateToken()
urlIFS = urlIFS_token['urlEndpoint']
tokenIFS = urlIFS_token['token']
header = {"Authorization":tokenIFS}

for elem in lista:
    # Get AddressId
    urlLocationSet = "https://"+urlIFS+"/main/ifsapplications/projection/v1/LocationHandling.svc/LocationSet(LocationId='"+str(elem['LocationId'])+"')"
    #print(urlLocationSet)
    #print(header)
    getLocationSet = requests.get(urlLocationSet,headers=header)
    if getLocationSet.status_code == 200:
        print('OK')
        getAddressId = getLocationSet.json()['VisitAddress']
        elem['AddressInfoId'] = getAddressId
        
        #Set Service Request
        urlServiceRequestSet = "https://"+urlIFS+"/main/ifsapplications/projection/v1/RequestHandling.svc/SrvRequestVirtualSet"
        body = json.dumps(elem)
        print(body)
        postServiceRequestSet = requests.post(urlServiceRequestSet, data=body,headers=header)
        #print(postServiceRequestSet)
        getObjkey = postServiceRequestSet.json()['Objkey']

        #Create Service Request
        urlCreateServiceRequestSet = "https://"+urlIFS+"/main/ifsapplications/projection/v1/RequestHandling.svc/SrvRequestVirtualSet(Objkey='"+getObjkey+"')/IfsApp.RequestHandling.SrvRequestVirtual_Finish"
        postServiceRequestSet = requests.post(urlCreateServiceRequestSet,headers=header)
        print(postServiceRequestSet.json()['NewReqId'])
        
    else:
        print('NOK: status',getLocationSet.status_code)
