# .github/workflows/mastodon-publisher.py
import requests
import feedparser
import json
import os
from urllib.parse import quote

def publish_to_mastodon():
    """
    Publishes latest blog posts to Mastodon (mas.to or any instance)
    """
    mastodon_instance = os.environ.get('MASTODON_INSTANCE', 'https://mas.to')
    access_token = os.environ['MASTODON_ACCESS_TOKEN']
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Load previously posted items to avoid duplicates
    try:
        with open('mastodon_posted_items.json', 'r') as f:
            posted_items = json.load(f)
    except FileNotFoundError:
        posted_items = []
    
    for entry in feed.entries[:1]:  # Post latest entry only
        if entry.link not in posted_items:
            # Create post content for Mastodon
            # Mastodon has a 500 character limit by default (configurable per instance)
            title = entry.title
            summary = entry.summary if hasattr(entry, 'summary') else ''
            link = entry.link
            
            # Format the toot content
            if len(summary) > 200:
                summary = summary[:197] + '...'
            
            # Add hashtags based on entry tags or categories
            hashtags = []
            if hasattr(entry, 'tags') and entry.tags:
                hashtags = [f"#{tag.term.replace(' ', '').replace('-', '').lower()}" 
                           for tag in entry.tags[:3]]  # Limit to 3 hashtags
            else:
                hashtags = ['#blog', '#tech', '#writing']
            
            hashtag_text = ' '.join(hashtags)
            
            # Construct the toot
            toot_content = f"{title}\n\n{summary}\n\n{link}\n\n{hashtag_text}"
            
            # Ensure we don't exceed character limit (500 chars for mas.to)
            if len(toot_content) > 490:  # Leave some margin
                # Truncate summary further
                available_chars = 490 - len(title) - len(link) - len(hashtag_text) - 8  # 8 for newlines/spacing
                if available_chars > 10:
                    summary = summary[:available_chars-3] + '...'
                else:
                    summary = ''
                toot_content = f"{title}\n\n{summary}\n\n{link}\n\n{hashtag_text}".strip()
            
            post_data = {
                'status': toot_content,
                'visibility': 'public',  # Options: public, unlisted, private, direct
                'language': 'en'
            }
            
            # Post to Mastodon
            response = requests.post(
                f'{mastodon_instance}/api/v1/statuses',
                headers=headers,
                json=post_data
            )
            
            if response.status_code == 200:
                posted_items.append(entry.link)
                toot_data = response.json()
                print(f"Successfully posted to Mastodon: {entry.title}")
                print(f"Toot URL: {toot_data.get('url', 'N/A')}")
            else:
                print(f"Failed to post to Mastodon: {entry.title}")
                print(f"Error: {response.status_code} - {response.text}")
    
    # Save updated posted items
    with open('mastodon_posted_items.json', 'w') as f:
        json.dump(posted_items, f)

def get_mastodon_instance_info():
    """
    Optional: Get instance information for debugging
    """
    mastodon_instance = os.environ.get('MASTODON_INSTANCE', 'https://mas.to')
    
    try:
        response = requests.get(f'{mastodon_instance}/api/v1/instance')
        if response.status_code == 200:
            instance_info = response.json()
            print(f"Instance: {instance_info.get('title', 'N/A')}")
            print(f"Character limit: {instance_info.get('max_toot_chars', 500)}")
            print(f"Version: {instance_info.get('version', 'N/A')}")
            return instance_info.get('max_toot_chars', 500)
    except Exception as e:
        print(f"Could not fetch instance info: {e}")
        return 500  # Default fallback

if __name__ == "__main__":
    # Optionally check instance info first
    # char_limit = get_mastodon_instance_info()
    
    publish_to_mastodon()
