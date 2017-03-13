import tweepy
from SETTINGS import *
import datetime


class Parser:
    tweets = []
    count = 0

    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.date = datetime.date.today()

        print 'Initiated for ' + str(self.date)

    def search(self):
        for x in range(0, len(KEYWORDS)):
            # results = self.api.GetSearch(raw_query="vertical=news&q=" + KEYWORDS[x] + "&src=typd")
            results = self.api.search(q=KEYWORDS[x], rpp=str(SEARCH_RETURN))
            self.count += len(results)
            print 'Total results: ' + str(self.count)
            print KEYWORDS[x]

            for y in range(0, len(results)):
                ID = results[y].id
                print ID
                retweets = len(self.api.retweets(ID))
                print retweets

                if retweets >= RETWEET_POPULARITY:
                    self.tweets.append(ID)
                    print 'Retweet made.'

            if len(self.tweets) > THRESHOLD:
                    break


    def retweet(self):
        for tweet in self.tweets:
            self.api.retweet(tweet)


if __name__ == '__main__':
    run = Parser()
    run.search()
    run.retweet()
