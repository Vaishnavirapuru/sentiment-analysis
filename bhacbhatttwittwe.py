import os
import pandas as pd
from datetime import date

today = date.today()
end_date = today
search_term = 'president'
from_date = '2019-01-01'


os.system(f"snscrape --since {from_date} twitter-search '{search_term} until:{end_date}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counter = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counter = df.size

print('Number Of Tweets : '+ str(counter))

max_results = 100

extracted_tweets = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-search '{search_term} until:{end_date}' > extracted-tweets.txt"
os.system(extracted_tweets)
if os.stat("extracted-tweets.txt").st_size == 0:
  print('No Tweets found')
else:
  df = pd.read_csv('extracted-tweets.txt', names=['content'])
  for row in df['content'].iteritems():
    print(row)

user_name = "realDonaldTrump"
user_tweets = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-user '{user_name} until:{end_date}' > user-tweets.txt"
os.system(user_tweets)
if os.stat("user-tweets.txt").st_size == 0:
  print('No Tweets found')
else:
  df = pd.read_csv('user-tweets.txt', names=['content'])
  for row in df['content'].iteritems():
    print(row)
