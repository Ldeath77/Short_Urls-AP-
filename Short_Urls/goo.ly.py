import json
import requests
import string
import pickle
import random
import time
GOOGLE_URL_SHORTEN_API = 'AIzaSyBdIIHReoZac9ltnZP173bMo_yl25U5IKQ '
google={}
def google_url_shorten(url):
   req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + GOOGLE_URL_SHORTEN_API
   payload = {'longUrl': url}
   headers = {'content-type': 'application/json'}
   r = requests.post(req_url, data=json.dumps(payload), headers=headers)
   resp = json.loads(r.text)
   return resp['id']
#response=google_url_shorten("https://stackoverflow.com/questions")
#print response
def google_url_expand(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?shortUrl=' + url + '&key=' + GOOGLE_URL_SHORTEN_API + '&projection=FULL'
    r = requests.get(req_url)
    response = json.loads(r.text)
    #print response
    if 'error' not in response:
        google[url]=response
        with open("C:\Users\KC-L\Documents\\googlecollection2.txt", "wb") as myFile:
            myFile.write(url + "\n")
            myFile.flush()
        print google[url]
while True:
    try:
        str1=''.join(random.choice(string.ascii_lowercase +string.ascii_uppercase + string.digits)for _ in range(6))
        url='https://goo.gl/'+str1
        #print url
        google_url_expand(url)
        time.sleep(1)
    except:
        continue
        time.sleep(300)
