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
with open("ServiceRequests_OK.txt", "a+") as myfile:
    myfile.write('[')
with open("ServiceRequests_NOK.txt", "a+") as myfile:
    myfile.write('[')


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
        #print(body)
        postServiceRequestSet = requests.post(urlServiceRequestSet, data=body,headers=header)
        print(postServiceRequestSet)
        if postServiceRequestSet.status_code == 201:
            getObjkey = postServiceRequestSet.json()['Objkey']

            #Create Service Request
            urlCreateServiceRequestSet = "https://"+urlIFS+"/main/ifsapplications/projection/v1/RequestHandling.svc/SrvRequestVirtualSet(Objkey='"+getObjkey+"')/IfsApp.RequestHandling.SrvRequestVirtual_Finish"
            postServiceRequestSet = requests.post(urlCreateServiceRequestSet,headers=header)
            if postServiceRequestSet.status_code ==201 or postServiceRequestSet.status_code==200:
                elem['NewReqId'] = postServiceRequestSet.json()['NewReqId']
                bodyDebug = json.dumps(elem)
                with open("ServiceRequests_OK.txt", "a+") as myfile:
                    myfile.write(bodyDebug+',')
                print(postServiceRequestSet.json()['NewReqId'])
                
                
                
            else:
                with open("ServiceRequests_NOK.txt", "a+") as myfile:
                    myfile.write(body)
                print('NOK___')
        
    else:
        print('NOK: status',getLocationSet.status_code)
        with open("ServiceRequests_NOK.txt", "w") as myfile:
            myfile.write(body+'\n'+getLocationSet.json())

with open("ServiceRequests_OK.txt", "a+") as myfile:
    myfile.write(']')
with open("ServiceRequests_NOK.txt", "a+") as myfile:
    myfile.write(']')
