# .github/workflows/twitter-publisher.py
import tweepy
import feedparser

def publish_to_twitter():
    client = tweepy.Client(
        consumer_key=os.environ['TWITTER_API_KEY'],
        consumer_secret=os.environ['TWITTER_API_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    for entry in feed.entries[:1]:
        tweet_text = f"{entry.title}\n\n{entry.link}"
        if len(tweet_text) <= 280:
            client.create_tweet(text=tweet_text)