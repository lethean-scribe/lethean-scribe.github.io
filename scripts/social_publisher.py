#!/usr/bin/env python3
"""
Social Media Publisher
Automated publishing to LinkedIn, Medium, Reddit, and X (Twitter)
"""

import os
import sys
import json
import time
import logging
import requests
import frontmatter
import markdown
from datetime import datetime
from urllib.parse import urljoin
from typing import Dict, List, Optional, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SocialMediaPublisher:
    """Main class for handling social media publishing"""
    
    def __init__(self, site_url: str):
        self.site_url = site_url
        self.platforms = {
            'linkedin': LinkedInPublisher(),
            'medium': MediumPublisher(),
            'reddit': RedditPublisher(),
            'twitter': TwitterPublisher()
        }
    
    def get_post_url(self, file_path: str) -> str:
        """Convert Jekyll post file path to URL"""
        filename = os.path.basename(file_path)
        if filename.endswith('.md'):
            filename = filename[:-3]
        
        parts = filename.split('-', 3)
        if len(parts) >= 4:
            year, month, day, title = parts[0], parts[1], parts[2], '-'.join(parts[3:])
            return f"{self.site_url}/{year}/{month}/{day}/{title}/"
        return f"{self.site_url}/"
    
    def publish_post(self, post_data: Dict[str, Any], platform: str) -> bool:
        """Publish a single post to a specific platform"""
        if platform not in self.platforms:
            logger.error(f"Unknown platform: {platform}")
            return False
        
        # Check if platform is enabled for this post
        social_config = post_data.get('social_media', {})
        platform_config = social_config.get(platform, False)
        
        if not platform_config:
            logger.info(f"Skipping {platform} for '{post_data['title']}' (not enabled)")
            return True  # Not an error, just skipped
        
        # Add post URL to post data
        post_data['url'] = self.get_post_url(post_data['file_path'])
        
        logger.info(f"Publishing '{post_data['title']}' to {platform}...")
        
        try:
            publisher = self.platforms[platform]
            return publisher.publish(post_data)
        except Exception as e:
            logger.error(f"Error publishing to {platform}: {e}")
            return False

class BasePlatformPublisher:
    """Base class for platform-specific publishers"""
    
    def __init__(self):
        self.rate_limiter = RateLimiter()
    
    def publish(self, post_data: Dict[str, Any]) -> bool:
        """Publish post to this platform"""
        raise NotImplementedError
    
    def validate_credentials(self) -> bool:
        """Validate that required credentials are available"""
        raise NotImplementedError

class LinkedInPublisher(BasePlatformPublisher):
    """LinkedIn publishing implementation"""
    
    def __init__(self):
        super().__init__()
        self.access_token = os.environ.get('LINKEDIN_ACCESS_TOKEN')
        self.person_id = os.environ.get('LINKEDIN_PERSON_ID')
    
    def validate_credentials(self) -> bool:
        return bool(self.access_token and self.person_id)
    
    def publish(self, post_data: Dict[str, Any]) -> bool:
        if not self.validate_credentials():
            logger.error("LinkedIn credentials not configured")
            return False
        
        # Wait for rate limiting
        self.rate_limiter.wait_if_needed('linkedin')
        
        url = "https://api.linkedin.com/v2/ugcPosts"
        
        # Format content for LinkedIn
        content = f"{post_data['title']}\n\n{post_data['excerpt']}\n\nRead more: {post_data['url']}"
        
        payload = {
            "author": f"urn:li:person:{self.person_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            if response.status_code == 201:
                logger.info(f"✅ Successfully published to LinkedIn: {post_data['title']}")
                return True
            else:
                logger.error(f"❌ LinkedIn API error: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            logger.error(f"❌ LinkedIn publishing error: {e}")
            return False

class MediumPublisher(BasePlatformPublisher):
    """Medium publishing implementation"""
    
    def __init__(self):
        super().__init__()
        self.access_token = os.environ.get('MEDIUM_ACCESS_TOKEN')
        self.user_id = os.environ.get('MEDIUM_USER_ID')
    
    def validate_credentials(self) -> bool:
        return bool(self.access_token)
    
    def get_user_id(self) -> Optional[str]:
        """Get Medium user ID if not provided"""
        if self.user_id:
            return self.user_id
        
        try:
            response = requests.get(
                "https://api.medium.com/v1/me",
                headers={'Authorization': f'Bearer {self.access_token}'},
                timeout=30
            )
            if response.status_code == 200:
                return response.json()['data']['id']
            else:
                logger.error(f"Could not get Medium user ID: {response.text}")
                return None
        except Exception as e:
            logger.error(f"Medium user ID error: {e}")
            return None
    
    def publish(self, post_data: Dict[str, Any]) -> bool:
        if not self.validate_credentials():
            logger.error("Medium credentials not configured")
            return False
        
        user_id = self.get_user_id()
        if not user_id:
            return False
        
        # Wait for rate limiting
        self.rate_limiter.wait_if_needed('medium')
        
        url = f"https://api.medium.com/v1/users/{user_id}/posts"
        
        # Convert markdown to HTML
        html_content = markdown.markdown(post_data['content'])
        html_content += f'\n\n<p><em>Originally published at <a href="{post_data["url"]}">{post_data["url"]}</a></em></p>'
        
        payload = {
            "title": post_data['title'],
            "contentFormat": "html",
            "content": html_content,
            "tags": post_data['tags'][:5],  # Medium allows max 5 tags
            "publishStatus": "public",
            "canonicalUrl": post_data['url']
        }
        
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            if response.status_code == 201:
                logger.info(f"✅ Successfully published to Medium: {post_data['title']}")
                return True
            else:
                logger.error(f"❌ Medium API error: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            logger.error(f"❌ Medium publishing error: {e}")
            return False

class RedditPublisher(BasePlatformPublisher):
    """Reddit publishing implementation"""
    
    def __init__(self):
        super().__init__()
        self.client_id = os.environ.get('REDDIT_CLIENT_ID')
        self.client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
        self.username = os.environ.get('REDDIT_USERNAME')
        self.password = os.environ.get('REDDIT_PASSWORD')
    
    def validate_credentials(self) -> bool:
        return all([self.client_id, self.client_secret, self.username, self.password])
    
    def publish(self, post_data: Dict[str, Any]) -> bool:
        if not self.validate_credentials():
            logger.error("Reddit credentials not configured")
            return False
        
        try:
            import praw
        except ImportError:
            logger.error("PRAW not installed for Reddit publishing")
            return False
        
        # Wait for rate limiting
        self.rate_limiter.wait_if_needed('reddit')
        
        try:
            reddit = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                username=self.username,
                password=self.password,
                user_agent='AutoPublisher/1.0'
            )
            
            # Get subreddit from post config or use default
            reddit_config = post_data['social_media'].get('reddit', {})
            subreddit_name = reddit_config.get('subreddit', 'programming')
            
            subreddit = reddit.subreddit(subreddit_name)
            
            # Create selftext post with link
            selftext = f"{post_data['excerpt']}\n\n[Read the full article]({post_data['url']})"
            
            submission = subreddit.submit(
                title=post_data['title'],
                selftext=selftext
            )
            
            if submission.id:
                logger.info(f"✅ Successfully published to Reddit r/{subreddit_name}: {post_data['title']}")
                return True
            else:
                logger.error("Reddit submission failed")
                return False
                
        except Exception as e:
            logger.error(f"❌ Reddit publishing error: {e}")
            return False

class TwitterPublisher(BasePlatformPublisher):
    """Twitter/X publishing implementation"""
    
    def __init__(self):
        super().__init__()
        self.api_key = os.environ.get('TWITTER_API_KEY')
        self.api_secret = os.environ.get('TWITTER_API_SECRET')
        self.access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    
    def validate_credentials(self) -> bool:
        return all([self.api_key, self.api_secret, self.access_token, self.access_token_secret])
    
    def publish(self, post_data: Dict[str, Any]) -> bool:
        if not self.validate_credentials():
            logger.error("Twitter credentials not configured")
            return False
        
        try:
            import tweepy
        except ImportError:
            logger.error("Tweepy not installed for Twitter publishing")
            return False
        
        # Wait for rate limiting
        self.rate_limiter.wait_if_needed('twitter')
        
        try:
            client = tweepy.Client(
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret
            )
            
            twitter_config = post_data['social_media'].get('twitter', {})
            hashtags = twitter_config.get('hashtags', [])
            
            # Format tweet
            hashtag_str = ' '.join(hashtags) if hashtags else ''
            tweet_text = f"{post_data['title']}\n\n{post_data['excerpt'][:150]}...\n\n{post_data['url']}"
            
            if hashtag_str:
                tweet_text += f"\n\n{hashtag_str}"
            
            # Ensure under 280 characters
            if len(tweet_text) > 280:
                # Truncate excerpt to fit
                available_chars = 280 - len(post_data['title']) - len(post_data['url']) - len(hashtag_str) - 10
                excerpt = post_data['excerpt'][:available_chars] + "..."
                tweet_text = f"{post_data['title']}\n\n{excerpt}\n\n{post_data['url']}"
                if hashtag_str:
                    tweet_text += f"\n\n{hashtag_str}"
            
            response = client.create_tweet(text=tweet_text)
            
            if response.data and response.data.get('id'):
                logger.info(f"✅ Successfully published to Twitter: {post_data['title']}")
                return True
            else:
                logger.error(f"Twitter API error: {response}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Twitter publishing error: {e}")
            return False

class RateLimiter:
    """Simple rate limiter to avoid API abuse"""
    
    def __init__(self):
        self.calls = {}
        self.limits = {
            'linkedin': {'calls': 100, 'window': 3600},  # 100 calls per hour
            'medium': {'calls': 100, 'window': 3600},    # 100 calls per hour
            'reddit': {'calls': 60, 'window': 3600},     # 60 calls per hour
            'twitter': {'calls': 300, 'window': 900}     # 300 calls per 15 minutes
        }
    
    def wait_if_needed(self, platform: str):
        """Wait if rate limit would be exceeded"""
        if platform not in self.limits:
            return
        
        now = time.time()
        limit_config = self.limits[platform]
        window = limit_config['window']
        max_calls = limit_config['calls']
        
        # Initialize platform tracking
        if platform not in self.calls:
            self.calls[platform] = []
        
        # Remove old calls outside the window
        self.calls[platform] = [
            call_time for call_time in self.calls[platform] 
            if call_time > now - window
        ]
        
        # Check if we need to wait
        if len(self.calls[platform]) >= max_calls:
            sleep_time = self.calls[platform][0] + window - now
            if sleep_time > 0:
                logger.info(f"Rate limit reached for {platform}, waiting {sleep_time:.1f} seconds")
                time.sleep(sleep_time)
        
        # Record this call
        self.calls[platform].append(now)

def main():
    """Main entry point for the script"""
    if len(sys.argv) < 3:
        print("Usage: python social_publisher.py <platform> <posts_json>")
        sys.exit(1)
    
    platform = sys.argv[1]
    posts_json = sys.argv[2]
    
    # Load configuration
    site_url = os.environ.get('SITE_URL', 'https://yourusername.github.io/auto-publisher-blog')
    
    try:
        posts_data = json.loads(posts_json)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON data: {e}")
        sys.exit(1)
    
    # Initialize publisher
    publisher = SocialMediaPublisher(site_url)
    
    # Publish posts
    success_count = 0
    total_posts = len(posts_data)
    
    for i, post_data in enumerate(posts_data):
        if i > 0:
            time.sleep(5)  # Delay between posts
        
        success = publisher.publish_post(post_data, platform)
        if success:
            success_count += 1
    
    logger.info(f"Publishing Summary for {platform}:")
    logger.info(f"  ✅ Successful: {success_count}")
    logger.info(f"  📝 Total posts: {total_posts}")
    
    # Exit with error code if no posts were successfully published
    if success_count == 0 and total_posts > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()

