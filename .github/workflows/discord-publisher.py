# .github/workflows/discord-publisher.py
import requests
import feedparser
import json

def publish_to_discord():
    webhook_url = os.environ['DISCORD_WEBHOOK_URL']
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    for entry in feed.entries[:1]:
        embed = {
            "embeds": [{
                "title": entry.title,
                "description": entry.summary[:2000],
                "url": entry.link,
                "color": 5814783,  # Blue color
                "footer": {
                    "text": "Lethean Scribe Blog"
                },
                "timestamp": entry.published
            }]
        }
        
        requests.post(webhook_url, json=embed)