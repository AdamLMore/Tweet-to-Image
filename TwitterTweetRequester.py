import time, threading
from TwitterAPI import TwitterAPI

consumer_key        = "your consumer_key here"
consumer_secret     = "your consumer_secret here"
access_token_key    = "your access_token_key here"
access_token_secret = "your access_token_secret here"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

##########################################################################
# Fetches the Tweets and prints

def requestTweets(search_term, count, will_print=False):
	r = api.request('search/tweets', {'q':search_term, 'count':count})
	for item in r.get_iterator():
		latest_id = item["id"]
        return_string = item["user"]["screen_name"] + "\n" + item["text"]
        if will_print:
            print return_string
        return return_string 

##########################################################################


