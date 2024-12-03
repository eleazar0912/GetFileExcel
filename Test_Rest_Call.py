# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:18:30 2024

@author: eleazar.ayaviri.carr
"""

import requests

header = {"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQY29mdGQ2YTgyalJXRlhXSlliMF82ajhGTFREQnhmRU1idF9Yd2FHaHBFIn0.eyJleHAiOjE3MzMxNTg5NDEsImlhdCI6MTczMzE1NTM0MSwianRpIjoiOTc3OWQ4NGUtNTRkMy00NzRjLWE0NmYtZjM4NWQyYWE2Y2E2IiwiaXNzIjoiaHR0cHM6Ly9yZHItdGVzdC5pZnNjbG91ZC5jb20udHIvYXV0aC9yZWFsbXMvcmRyLXRlc3QiLCJhdWQiOlsicmRyLXRlc3QiLCJhY2NvdW50Il0sInN1YiI6IjQ2ODA2M2FiLTE2ZmMtNDc1NC1hODNlLTI0ZmFmMTc3OGU2NyIsInR5cCI6IkJlYXJlciIsImF6cCI6IlBPU1RNQU4iLCJzZXNzaW9uX3N0YXRlIjoiOTMxN2EwNTktNDc4Ny00ZmVmLWJmYWItZDVjYjBjNzA3ODRiIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwiZGVmYXVsdC1yb2xlcy1yZHItdGVzdCIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgYXVkaWVuY2UgZW1haWwgbWljcm9wcm9maWxlLWp3dCBwcm9maWxlIiwic2lkIjoiOTMxN2EwNTktNDc4Ny00ZmVmLWJmYWItZDVjYjBjNzA3ODRiIiwidXBuIjoicG9zdG1hbiIsImNsaWVudEhvc3QiOiIxOTIuMTY4LjEyMi4xIiwiY2xpZW50SWQiOiJQT1NUTUFOIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJncm91cHMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXJkci10ZXN0IiwidW1hX2F1dGhvcml6YXRpb24iXSwicHJlZmVycmVkX3VzZXJuYW1lIjoicG9zdG1hbiIsImNsaWVudEFkZHJlc3MiOiIxOTIuMTY4LjEyMi4xIn0.XjudRayetlRjvIDFb_F0keaFlvg3B6aAVlYypRCENlN7Zi9GVBxtkCSEUjIKbJtV6uGZkJSMeH4SKKCDm55DNwZCOlkuXbGGNK1fiG8KOnqMOoGp51PCS_4q16gCkAyecIb9JrYxmNeibS5NGs88jQ1Ch8U3ZbAiOVHx5d6dC45ljGmhsWxnwmSgDPOlyx2hjgKOe3b2antcmg5Af92t2WniCmBHiqbpOjmDzDKUoJazhsHSRy7vQHdatYDfmTJ-5niEJL3WTyh1r8YDTFpeu2jsvjhV6766QGK8w9c1EX0kpn1I1666BjrptEKMW8T_oxD1pJEMakSxcUhHVCur4g"}

getServReq = requests.get("https://rdr-test.ifscloud.com.tr/main/ifsapplications/projection/v1/RequestHandling.svc/SrvRequestSet(ReqId='200')", headers=header)

print(getServReq.json())


headers = {'Content-Type': 'application/x-www-form-urlencoded'}

tokenEndpoint = "https://rdr-test.ifscloud.com.tr/auth/realms/rdr-test/protocol/openid-connect/token"
request_body = {
                "grant_type": "client_credentials",
                "client_id": "POSTMAN",
                "client_secret": "d66XQU0pqebi3oshXfksdvxNOjMctDTc",
                "scope": "openid microprofile-jwt"
        }

response = requests.post(tokenEndpoint, data=request_body,headers=headers)
token = response.json()['access_token']

print(token)