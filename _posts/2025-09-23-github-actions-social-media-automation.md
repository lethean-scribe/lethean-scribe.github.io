---
layout: post
title: "Building Social Media Automation with GitHub Actions"
date: 2025-09-23 14:30:00 +0000
categories: [development, automation, github]
tags: [github-actions, api, python, automation, devops]
author: "Auto Publisher"
excerpt: "Learn how to build a robust social media automation system using GitHub Actions, Python, and social media APIs. Complete with code examples and best practices."
social_media:
  linkedin: true
  medium: true
  reddit: 
    enabled: true
    subreddit: "programming"
  twitter: 
    enabled: true
    hashtags: ["#GitHubActions", "#automation", "#python", "#devops"]
---

GitHub Actions provides an excellent platform for automating social media publishing. In this post, we'll explore how to build a robust system that can handle multiple platforms reliably.

## Architecture Overview

Our automation system consists of several key components:

```yaml
# .github/workflows/publish-to-social.yml
name: Publish to Social Media
on:
  push:
    branches: [main]
    paths: ['_posts/**']
```

## The Publishing Workflow

### 1. Detect New Posts

The workflow first identifies which posts are new or updated:

```python
import os
import git
from datetime import datetime

def get_new_posts():
    repo = git.Repo('.')
    # Get files changed in the last commit
    changed_files = repo.git.diff('HEAD~1', 'HEAD', name_only=True).split('\n')
    
    new_posts = []
    for file in changed_files:
        if file.startswith('_posts/') and file.endswith('.md'):
            new_posts.append(file)
    
    return new_posts
```

### 2. Parse Post Metadata

Extract the front matter and content for each platform:

```python
import yaml
import markdown

def parse_post(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split front matter and content
    parts = content.split('---', 2)
    front_matter = yaml.safe_load(parts[1])
    post_content = parts[2].strip()
    
    return {
        'title': front_matter.get('title'),
        'excerpt': front_matter.get('excerpt'),
        'tags': front_matter.get('tags', []),
        'categories': front_matter.get('categories', []),
        'content': post_content,
        'social_media': front_matter.get('social_media', {})
    }
```

### 3. Platform-Specific Publishing

Each platform requires different formatting and API calls:

#### LinkedIn Publishing

```python
import requests

def publish_to_linkedin(post_data, access_token):
    url = "https://api.linkedin.com/v2/ugcPosts"
    
    # Format content for LinkedIn
    content = f"{post_data['title']}\n\n{post_data['excerpt']}\n\nRead more: {post_data['url']}"
    
    payload = {
        "author": f"urn:li:person:{person_id}",
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
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 201
```

#### Medium Publishing

```python
def publish_to_medium(post_data, access_token):
    url = f"https://api.medium.com/v1/users/{user_id}/posts"
    
    # Convert markdown to HTML for Medium
    html_content = markdown.markdown(post_data['content'])
    
    payload = {
        "title": post_data['title'],
        "contentFormat": "html",
        "content": html_content,
        "tags": post_data['tags'][:5],  # Medium allows max 5 tags
        "publishStatus": "public"
    }
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 201
```

#### Reddit Publishing

```python
import praw

def publish_to_reddit(post_data, reddit_config):
    reddit = praw.Reddit(
        client_id=reddit_config['client_id'],
        client_secret=reddit_config['client_secret'],
        username=reddit_config['username'],
        password=reddit_config['password'],
        user_agent='AutoPublisher/1.0'
    )
    
    subreddit = reddit.subreddit(post_data['social_media']['reddit']['subreddit'])
    
    # Create a text post with link
    title = post_data['title']
    content = f"{post_data['excerpt']}\n\n[Read the full article]({post_data['url']})"
    
    submission = subreddit.submit(title=title, selftext=content)
    return submission.id is not None
```

#### X (Twitter) Publishing

```python
import tweepy

def publish_to_twitter(post_data, twitter_config):
    client = tweepy.Client(
        consumer_key=twitter_config['api_key'],
        consumer_secret=twitter_config['api_secret'],
        access_token=twitter_config['access_token'],
        access_token_secret=twitter_config['access_token_secret']
    )
    
    # Format tweet with character limit
    hashtags = ' '.join(post_data['social_media']['twitter']['hashtags'])
    tweet_text = f"{post_data['title']}\n\n{post_data['excerpt'][:200]}...\n\n{post_data['url']} {hashtags}"
    
    # Ensure under 280 characters
    if len(tweet_text) > 280:
        tweet_text = tweet_text[:276] + "..."
    
    response = client.create_tweet(text=tweet_text)
    return response.data['id'] is not None
```

## Error Handling and Retry Logic

Robust automation requires proper error handling:

```python
import time
from functools import wraps

def retry_on_failure(max_retries=3, delay=5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay * (attempt + 1))
            return None
        return wrapper
    return decorator

@retry_on_failure(max_retries=3)
def publish_with_retry(platform, post_data, config):
    if platform == 'linkedin':
        return publish_to_linkedin(post_data, config['access_token'])
    elif platform == 'medium':
        return publish_to_medium(post_data, config['access_token'])
    # ... other platforms
```

## Security Best Practices

### 1. Use GitHub Secrets

Store all API credentials as GitHub repository secrets:

```yaml
env:
  LINKEDIN_ACCESS_TOKEN: ${{ secrets.LINKEDIN_ACCESS_TOKEN }}
  MEDIUM_ACCESS_TOKEN: ${{ secrets.MEDIUM_ACCESS_TOKEN }}
  REDDIT_CLIENT_ID: ${{ secrets.REDDIT_CLIENT_ID }}
  TWITTER_API_KEY: ${{ secrets.TWITTER_API_KEY }}
```

### 2. Validate Input Data

Always validate and sanitize content before publishing:

```python
def validate_post_data(post_data):
    required_fields = ['title', 'content', 'url']
    for field in required_fields:
        if not post_data.get(field):
            raise ValueError(f"Missing required field: {field}")
    
    # Sanitize content
    post_data['title'] = post_data['title'].strip()
    post_data['content'] = post_data['content'].strip()
    
    return post_data
```

### 3. Rate Limiting

Respect API rate limits to avoid being blocked:

```python
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self):
        self.calls = defaultdict(list)
    
    def wait_if_needed(self, platform, max_calls_per_hour=100):
        now = time.time()
        hour_ago = now - 3600
        
        # Remove old calls
        self.calls[platform] = [call_time for call_time in self.calls[platform] if call_time > hour_ago]
        
        # Check if we need to wait
        if len(self.calls[platform]) >= max_calls_per_hour:
            sleep_time = self.calls[platform][0] + 3600 - now
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        self.calls[platform].append(now)
```

## Monitoring and Logging

Track the success and failure of your automation:

```python
import logging
import json

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def log_publishing_result(platform, post_title, success, error=None):
    logger = setup_logging()
    
    result = {
        'platform': platform,
        'post_title': post_title,
        'success': success,
        'timestamp': time.time()
    }
    
    if error:
        result['error'] = str(error)
        logger.error(f"Failed to publish to {platform}: {error}")
    else:
        logger.info(f"Successfully published to {platform}: {post_title}")
    
    # Store results for analytics
    with open('publishing_log.json', 'a') as f:
        f.write(json.dumps(result) + '\n')
```

## Next Steps

In our next post, we'll cover:

- Setting up webhook notifications for publishing status
- Building a dashboard to monitor cross-platform performance
- Advanced content customization for different audiences
- Handling platform-specific content requirements

The complete source code for this automation system is available in our [GitHub repository](https://github.com/yourusername/auto-publisher-blog).

---

*This technical deep-dive was automatically shared across LinkedIn, Medium, Reddit, and X. Each platform received a customized version optimized for its audience and format requirements.*

