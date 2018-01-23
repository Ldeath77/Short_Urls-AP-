import pickle
import json
import requests
import string
import pickle
import random
import time
from urlunshort import resolve
with open("C:\Users\KC-L\Documents\\twitter_collection.txt", "rb") as myFile:
    dic = myFile.readlines()
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
        "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING","UNWANTED_SOFTWARE","POTENTIALLY_HARMFUL_APPLICATION"],
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
domain = raw_input()
#domain = "https://goo.gl/"
while True:
    try:
        rand=''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)for _ in range(3))
        rand='6n'+rand
        print rand
        url = domain + rand
        #print url
        r = requests.get(url)
        #print requests
        status = r.status_code
        print status
        if status != 404 and status != 403:
            file = open("C:\Users\KC-L\Documents\\qgs_collection", "a")
            file.write(url+'\n')
            file.write(resolve(url))
            print url
            file.flush()
            new=resolve(url)
            print new
            resp=google_url_shorten(new)
            print resp
            if len(resp) != 0:
                malicious[k] = resp
                print malicious[k]
            with open("C:\Users\KC-L\Documents\maliciouscollection2.txt", "wb") as myFile:
                pickle.dump(malicious, myFile)
    except:
        continue
        time.sleep(1)
#for k in dic:
 #   print k[:-2]
  #  print type(k)
   # print resolve("http://rlu.ru/10zQZ")