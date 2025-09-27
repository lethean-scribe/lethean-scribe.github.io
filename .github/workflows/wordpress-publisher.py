# .github/workflows/wordpress-publisher.py
import requests
import feedparser
import json
import os
import base64
from datetime import datetime

def publish_to_wordpress_com():
    site_id = os.environ['WORDPRESS_SITE_ID']  # Your WordPress.com site ID
    access_token = os.environ['WORDPRESS_ACCESS_TOKEN']
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Load previously posted items to avoid duplicates
    try:
        with open('wordpress_posted_items.json', 'r') as f:
            posted_items = json.load(f)
    except FileNotFoundError:
        posted_items = []
    
    for entry in feed.entries[:3]:  # Process last 3 posts
        if entry.link not in posted_items:
            # Convert content for WordPress
            wordpress_content = f"""
            <p><em>Originally published at: <a href="{entry.link}">{entry.link}</a></em></p>
            
            {entry.content[0].value if hasattr(entry, 'content') else entry.summary}
            
            <p><strong>Read the full article on our blog: <a href="{entry.link}">Continue reading...</a></strong></p>
            """
            
            post_data = {
                'title': entry.title,
                'content': wordpress_content,
                'status': 'publish',
                'type': 'post',
                'format': 'standard',
                'categories': ['Blog', 'Tech'],  # Adjust categories as needed
                'tags': getattr(entry, 'tags', []),
                'excerpt': entry.summary[:150] + '...' if len(entry.summary) > 150 else entry.summary,
                'featured_media': None,  # Add featured image ID if available
                'comment_status': 'open',
                'ping_status': 'open'
            }
            
            # Create the post
            response = requests.post(
                f'https://public-api.wordpress.com/rest/v1.1/sites/{site_id}/posts/new',
                headers=headers,
                json=post_data
            )
            
            if response.status_code == 200:
                posted_items.append(entry.link)
                print(f"Successfully published: {entry.title}")
            else:
                print(f"Failed to publish {entry.title}: {response.text}")
    
    # Save updated posted items
    with open('wordpress_posted_items.json', 'w') as f:
        json.dump(posted_items, f)

if __name__ == "__main__":
    publish_to_wordpress_com()