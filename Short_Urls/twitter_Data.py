import tweepy
import pickle
import time
from xml.sax.saxutils import escape, unescape
consumer_key = 'cUkpXYkWXD3rHQ3WJK4DknfGP'
consumer_secret = 'YHM3lFk36tYs2EeYBVSX8vh9vfUAtAIg2ghgHbi5PefIMQg12G'
access_token = '853260796230586373-2mMbLwzvg2aE0zcuCHwfrhJzJ1h6tks'
access_token_secret = 'kZcNgcOZB662fZ9yBbDknQHMHGVcnciMfUmsMJrFEvTd6'

TweetCollection={}
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #alltweets = api.user_timeline(screen_name=screen_name, count=200, include_entities=True, tweet_mode='extended')
    #alltweets=tweepy.Cursor(api.user_timeline, screen_name=screen_name).items(200)
    #print alltweets
    for tweet in limit_handled(tweepy.Cursor(api.user_timeline, screen_name=screen_name).items(3200)):
        Id=tweet.id_str
        PublishedAt=str(tweet.created_at)
        Tweet=unescape(tweet.text)
        ScreenName=screen_name
        if tweet.entities['urls']!=[]:
            Url=tweet.entities['urls'][0].get('url')
            #print Url
            display_url=tweet.entities['urls'][0].get('display_url')
            expanded_url=tweet.entities['urls'][0].get('expanded_url')
        else:
            Url=None
        if Id is not None and Url not in TweetCollection and Url is not None:
            TweetCollection[Url]={'Tweet': Tweet, 'ScreenName': ScreenName, 'Url': Url,'display_url':display_url,'expanded_url':expanded_url, 'PublishedAt': PublishedAt}
            #print Id
            #print Url,display_url,expanded_url
            print Url
            file = open("C:\Users\KC-L\Documents\\twitter_collection.txt", "a")
            file.write(Url + "\n")
            file.flush()
get_all_tweets('@realDonaldTrump')
get_all_tweets('@imVkohli')
get_all_tweets('@narendramodi')
get_all_tweets('@msdhoni')
get_all_tweets('@AjitPaiFCC')
get_all_tweets('@WhatsTrending')
#print TweetCollection
