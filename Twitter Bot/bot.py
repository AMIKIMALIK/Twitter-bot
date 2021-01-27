import tweepy
import time


auth= tweepy.OAuthHandler('','')

auth.set_access_token('','')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# api.update_status("Twitter bot reporting in live")

user =api.me()

# print(user.screen_name)

# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)
#     # if follower.name == "Amalik":
#     #       follower.follow()

Search= ["100DaysOfCode"]
nrTweets = 500

for tweet in tweepy.Cursor(api.search, Search).items(nrTweets):
     try:
          print("Retweet!")
          # tweet.favorite()
          tweet.retweet()
          time.sleep(60)
     except tweepy.TweepError as e:
          print(e.reason)
     except StopIteration:
          break

