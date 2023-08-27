import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import praw
my_client_id = '' ####71gyA7wz3qo6NU80MHiDmg
my_client_secret = '' ####C_p0RfVPKlNI4operIjnYhy0GwJsIA
my_user_agent = 'webscrap'
posts = []
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)
ml_subreddit = reddit.subreddit('college')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
print(posts)



