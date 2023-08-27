import twint

# Configure
c = twint.Config()
c.Username = "sonusood"
c.Limit = 1

# Run
twint.run.Search(c)
import nest_asyncio
nest_asyncio.apply()


# c = twint.Config()
# c.Limit = 1
# c.Username = 'AnuragUniversi'
# c.Min_likes = 30000
c.Pandas = True

twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df
