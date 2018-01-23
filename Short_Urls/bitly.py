import bitly_api
import string
import pickle
import random
import time
bitlyCollection={}
connex = bitly_api.Connection(access_token="120c9b5af75314f6f58e4af8e9904d6527b95351")
while True:
    try:
        rand=''.join(random.choice(string.ascii_lowercase +string.ascii_uppercase + string.digits)for _ in range(6))
        print rand
        response1 = connex.expand(rand)
        #print response1
        if 'error' not in response1[0]:
            if response1[0]['long_url']:
                long_url=response1[0]['long_url']
                #print long_url
                response2=connex.link_lookup(long_url)
                short_url=response2[0]['aggregate_link']
                print short_url
                if short_url not in bitlyCollection:
                    bitlyCollection[short_url]={'Url':short_url,'expanded_url':long_url,'hash':rand}
    except:
        continue
        time.sleep(60*60)
    with open("C:\Users\KC-L\Documents\\bitlycollection.txt", "wb") as myFile:
        pickle.dump(TweetCollection, myFile)