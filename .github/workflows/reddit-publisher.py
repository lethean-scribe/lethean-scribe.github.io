# .github/workflows/reddit-publisher.py
import praw
import feedparser
import json
import os

def publish_to_reddit():
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_CLIENT_SECRET'],
        user_agent=os.environ['REDDIT_USER_AGENT'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD']
    )
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    # Load previously posted items
    try:
        with open('posted_items.json', 'r') as f:
            posted_items = json.load(f)
    except FileNotFoundError:
        posted_items = []
    
    for entry in feed.entries[:3]:  # Last 3 posts
        if entry.link not in posted_items:
            subreddit = reddit.subreddit('your_subreddit')
            subreddit.submit(title=entry.title, url=entry.link)
            posted_items.append(entry.link)
    
    # Save updated posted items
    with open('posted_items.json', 'w') as f:
        json.dump(posted_items, f)

if __name__ == "__main__":
    publish_to_reddit()