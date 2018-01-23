import json
import requests
import string
import pickle
import random
import time
from urlunshort import resolve
#key = " AIzaSyDwGng97aN8ZhKR32grwd41UPEqGWyISac "
#URL = "https://sb-ssl.google.com/safebrowsing/api/lookup?client=python&apikey={key}&appver=1.0&pver=3.0&url={url}"
with open("C:\Users\KC-L\Documents\\bitl", "rb") as myFile:
    dic = myFile.readlines()
#print dic
malicious={}
GOOGLE_URL_SHORTEN_API = ' AIzaSyDwGng97aN8ZhKR32grwd41UPEqGWyISac  '
google={}
def google_url_shorten(url):
   req_url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=' + GOOGLE_URL_SHORTEN_API
   payload = {
    "client": {
        "clientId": "yourcompanyname",
        "clientVersion": "1.5.2"
    },
    "threatInfo": {
        "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
        "platformTypes": ["ALL_PLATFORMS"],
        "threatEntryTypes": ["URL"],
        "threatEntries": [
            {"url": url},
        ]
    }
}
   headers = {'content-type': 'application/json'}
   r = requests.post(req_url, data=json.dumps(payload), headers=headers)
   resp = json.loads(r.text)
   return resp
for k in dic:
    print k
    k=resolve(k[:-2])
    #print hum
    resp=google_url_shorten(k)
    #print resp
    if len(resp) != 0:
        malicious[k]=resp
        print malicious[k]
    with open("C:\Users\KC-L\Documents\maliciouscollection1.txt", "wb") as myFile:
        pickle.dump(malicious, myFile)

