from facebook_scraper import get_posts
import pandas as pd
import facebook_scraper as fs
listposts = []

for post in get_posts("Anuraguniversity", pages=10):
    print(post['text'][:50])
    listposts.append(post)

#posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(listposts)
