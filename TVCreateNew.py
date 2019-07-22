'''
A 130Tech® Product 1999 - 2019 All Rights Reserved
TV Create New Device 
Creates New Device in TV
Note : you must have the correct permissions with TV to use this
Im usin Oython 3.7 64bit to run this.
'''
import requests
from requests.auth import HTTPDigestAuth
import json

def createNewDevice():
#RAW INPUTS
    print("130Tech® TeamViewer Reports - Device Add v0.0.1")
    print("Creating New Device, Please Wait...")
    #Inputs
    remoteID = input("Enter Remote ID:")
    groupID = input("Enter Group ID:")
    descr = input("Enter Description;")
    alias = input("Enter Alias:")
    pword = input("Enter Password:")
    #REST 
    url="https://webapi.teamviewer.com/api/v1/devices" 
    #setup headers
    headers = {"content-type": "application/json", "Authorization": "Bearer you'll need to get this from TeamViewer"
    #Set it Up
    data = {"remotecontrol_id": remoteID, "groupid" : groupID, "description" : descr, "alias" : alias, "password" : pword}
    #POST    
    r = requests.post(url, headers=headers,json=data)
    myResult = r.json() #If success just show what we did
    print(myResult)
#That's it
print("Done")
createNewDevice()
