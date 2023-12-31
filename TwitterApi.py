import tweepy
import sys
import json
# access_token="1470052853196591107-1ccsdx0KWm1JNNu6qsCnU1HSUP5Ksq"
# access_token_secret="Bp2R51lI10cwe0xk5knrHaBPfZ0SWDO4gpDjuh3m0JOwA"
# consumer_key="3AVViVnnaX1ouzAcKLPd06k35"
# consumer_secret="NzsKejKoXZagJ05hT1a1LBCDQPp1GhIOaqxQJjQZvaWbg3LZzl"
# auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)


# authorization tokens
# consumer_key = 'IKQH0zPM14fHE3KsgRlwu2zqz'
# consumer_secret = 'BfjBgRU3yfzWqyWYl5EtEbu5vKzE9FLzq2XxNbABXisOjPbuw5'
# access_key = "1470052853196591107-TorDHQUxKgeXGCjIjbaTfO9zVhFDt8"
# access_secret = "LV3RTEvierbbLvji7x3AsbteleufrzHy8ntq1GIcaZ0m7"

# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status,"extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text

        # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status,"extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text

        # remove characters that might cause problems with csv encoding
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")

        with open("out.csv", "a", encoding='utf-8') as f:
            f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,is_retweet,is_quote,text,quoted_text))

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    with open("out.csv", "w", encoding='utf-8') as f:
        f.write("date,user,is_retweet,is_quote,text,quoted_text\n")
    tags = ["anurag univeristy"]
    stream.filter(track=tags)
