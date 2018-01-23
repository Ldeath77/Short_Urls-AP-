import json
import urllib
import requests
import seolib as seo
import pickle
import schedule
import time
localtime = time.localtime(time.time())
# API keys
api_key="262710c67ec4aa53a86d680777377934144310f3609059a219565e0eada12264"
GOOGLE_URL_SHORTEN_API = ' AIzaSyDwGng97aN8ZhKR32grwd41UPEqGWyISac  '
# globals
mal={}
fin={}
#Get report from google safe browsing
def google_report(url):
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
# get alexa rank
def alexa_rank(url):
    alexa_rank = seo.get_alexa(url)
    if alexa_rank:
        return alexa_rank
    else:
        return "error"
#getting malicious urls from virus total
def get_mal_url(domain,api_key):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    parameters = {'domain': domain, 'apikey': api_key}
    response = requests.get(url, params=parameters)
    # response_dict = json.loads(response)
    res = response.json()
    #print res
    mal[domain]=res
    with open("C:\Users\KC-L\Documents\Short_Urls\Virus_mal_collection"+str(localtime[2])+str(localtime[3])+".txt", "wb") as myFile:
        pickle.dump(mal, myFile)
    #with open("C:\Users\KC-L\Documents\Short_Urls\\data.txt", "a") as myFile:
        k=1
        for i in res["detected_urls"]:
            print i["url"]
            print k
            k+=1
            if i["url"] not in fin:
                status=get_chain(i["url"],domain)
            #myFile.write(i["url"] + "\n")
            #myFile.flush()
    return "done"
    #myFile.close()
# determinig redirect chain
def get_chain(url,domain):
    try:
        #print url
        r = requests.get(url)
        if len(r.history) > 0:
            chain = ""
            code = r.history[0].status_code
            final_url = r.url
            fin[url]={}
            fin[url]["domain"]=domain
            fin[url]["len_init_url"] = len(url)
            fin[url]["dest_url"]=r.url
            fin[url]["len_dest_url"]=len(r.url)
            fin[url]["redirect_message"]=r.history
            fin[url]["chain_count"]=len(r.history)
            fin[url]["alexa_ranking"]=alexa_rank(url)
            blacklist=google_report(url)
            if len(blacklist)>0:
                fin[url]["google_report_flag"]=1
            fin[url]["chain"]=[]
            for resp in r.history:
                fin[url]["chain"].append(resp.url)
            fin[url]["chain"].append(r.url)
            #print fin
            with open("C:\Users\KC-L\Documents\Short_Urls\Final"+str(localtime[2])+str(localtime[3])+".txt", "wb") as myFile:
                pickle.dump(fin, myFile)
            return "Done"
        else:
            return "No redirect"
    #except requests.ConnectionError:
     #   print("Error: failed to connect.")
     #   return '0'
    except:
        pass
def job():
    print "started"
    get_mal_url("bit.ly",api_key)
    print "bitly done"
    get_mal_url("t.co",api_key)
    print "twitter done"
    get_mal_url("x.co",api_key)
    print "x.co done"
    get_mal_url("bit.do",api_key)
    print "bit.do done"
    get_mal_url("is.gd",api_key)
    print "id good done"
    get_mal_url("rlu.ru",api_key)
    print "rlu.ru done"
    get_mal_url("goo.gl",api_key)
    print "google done"
    get_mal_url("u.nu",api_key)
    print "u.nu done"

while True:
    job()
    time.sleep(60*60*5)
#with open("C:\Users\KC-L\Documents\Short_Urls\\data.txt", "r") as myFile:
#    uniquelines=set(myFile.readlines())
#open("C:\Users\KC-L\Documents\Short_Urls\\data.txt",'w').writelines(uniquelines)
