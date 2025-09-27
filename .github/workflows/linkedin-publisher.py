# .github/workflows/linkedin-publisher.py
import requests
import feedparser
import json
import os

def publish_to_linkedin():
    access_token = os.environ['LINKEDIN_ACCESS_TOKEN']
    person_urn = os.environ['LINKEDIN_PERSON_URN']
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    
    for entry in feed.entries[:1]:  # Latest post only
        post_data = {
            "author": person_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": f"{entry.title}\n\n{entry.summary[:200]}..."
                    },
                    "shareMediaCategory": "ARTICLE",
                    "media": [{
                        "status": "READY",
                        "description": {
                            "text": entry.summary
                        },
                        "originalUrl": entry.link,
                        "title": {
                            "text": entry.title
                        }
                    }]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        response = requests.post(
            'https://api.linkedin.com/v2/ugcPosts',
            headers=headers,
            json=post_data
        )

if __name__ == "__main__":
    publish_to_linkedin()