#!/usr/bin/env python3
"""
Integration Testing Script
Test your social media API credentials before deploying
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any

# Try to load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Using system environment variables only.")

# Import our publisher classes
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from social_publisher import SocialMediaPublisher, LinkedInPublisher, MediumPublisher, RedditPublisher, TwitterPublisher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_test_post() -> Dict[str, Any]:
    """Create a test post for integration testing"""
    return {
        'title': 'Test Post - Auto Publisher Integration',
        'excerpt': 'This is a test post to verify that the Auto Publisher Blog integration is working correctly. If you see this, the automation is functioning!',
        'content': '''# Test Post

This is a test post created by the Auto Publisher Blog integration testing script.

## Purpose

This post verifies that:
- API credentials are correctly configured
- Content formatting works properly
- Publishing automation is functional

## Next Steps

If you see this post on the social media platform, your integration is working correctly!

You can now:
1. Delete this test post if desired
2. Start creating real content
3. Enjoy automated cross-platform publishing

---

*This was an automated test post. Learn more about Auto Publisher Blog at: https://github.com/yourusername/auto-publisher-blog*
''',
        'tags': ['test', 'automation', 'blog'],
        'categories': ['testing'],
        'file_path': '_posts/2025-09-23-test-integration.md',
        'social_media': {
            'linkedin': True,
            'medium': True,
            'reddit': {
                'enabled': True,
                'subreddit': 'test'  # Use test subreddit for testing
            },
            'twitter': {
                'enabled': True,
                'hashtags': ['#test', '#automation']
            }
        }
    }

def test_credentials():
    """Test API credentials for all platforms"""
    results = {}
    
    print("🔍 Testing API Credentials...\n")
    
    # Test LinkedIn
    print("📘 Testing LinkedIn...")
    linkedin = LinkedInPublisher()
    if linkedin.validate_credentials():
        print("✅ LinkedIn credentials found")
        results['linkedin'] = 'credentials_ok'
    else:
        print("❌ LinkedIn credentials missing or invalid")
        print("   Required: LINKEDIN_ACCESS_TOKEN, LINKEDIN_PERSON_ID")
        results['linkedin'] = 'credentials_missing'
    
    # Test Medium
    print("\n📝 Testing Medium...")
    medium = MediumPublisher()
    if medium.validate_credentials():
        print("✅ Medium credentials found")
        results['medium'] = 'credentials_ok'
    else:
        print("❌ Medium credentials missing or invalid")
        print("   Required: MEDIUM_ACCESS_TOKEN")
        results['medium'] = 'credentials_missing'
    
    # Test Reddit
    print("\n🔴 Testing Reddit...")
    reddit = RedditPublisher()
    if reddit.validate_credentials():
        print("✅ Reddit credentials found")
        results['reddit'] = 'credentials_ok'
    else:
        print("❌ Reddit credentials missing or invalid")
        print("   Required: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD")
        results['reddit'] = 'credentials_missing'
    
    # Test Twitter
    print("\n🐦 Testing Twitter...")
    twitter = TwitterPublisher()
    if twitter.validate_credentials():
        print("✅ Twitter credentials found")
        results['twitter'] = 'credentials_ok'
    else:
        print("❌ Twitter credentials missing or invalid")
        print("   Required: TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET")
        results['twitter'] = 'credentials_missing'
    
    return results

def test_publishing(platforms=None, dry_run=True):
    """Test publishing to specified platforms"""
    if platforms is None:
        platforms = ['linkedin', 'medium', 'reddit', 'twitter']
    
    site_url = os.environ.get('SITE_URL', 'https://yourusername.github.io/auto-publisher-blog')
    publisher = SocialMediaPublisher(site_url)
    test_post = create_test_post()
    
    print(f"\n🚀 Testing Publishing ({'DRY RUN' if dry_run else 'LIVE'})...\n")
    
    if dry_run:
        print("⚠️  DRY RUN MODE: No actual posts will be published")
        print("   Use --live flag to publish real test posts\n")
    
    results = {}
    
    for platform in platforms:
        print(f"📤 Testing {platform}...")
        
        # Check if credentials are available
        platform_publisher = publisher.platforms[platform]
        if not platform_publisher.validate_credentials():
            print(f"❌ Skipping {platform} - credentials not configured")
            results[platform] = 'skipped'
            continue
        
        if dry_run:
            print(f"✅ {platform} - credentials valid, would publish: '{test_post['title']}'")
            results[platform] = 'dry_run_ok'
        else:
            try:
                success = publisher.publish_post(test_post, platform)
                if success:
                    print(f"✅ Successfully published test post to {platform}")
                    results[platform] = 'published'
                else:
                    print(f"❌ Failed to publish to {platform}")
                    results[platform] = 'failed'
            except Exception as e:
                print(f"❌ Error publishing to {platform}: {e}")
                results[platform] = 'error'
        
        print()
    
    return results

def print_summary(credential_results, publishing_results=None):
    """Print a summary of test results"""
    print("\n" + "="*50)
    print("📊 INTEGRATION TEST SUMMARY")
    print("="*50)
    
    # Credentials summary
    print("\n🔑 Credentials Status:")
    for platform, status in credential_results.items():
        icon = "✅" if status == 'credentials_ok' else "❌"
        print(f"   {icon} {platform.capitalize()}: {status}")
    
    # Publishing summary
    if publishing_results:
        print("\n📤 Publishing Test Results:")
        for platform, status in publishing_results.items():
            if status == 'skipped':
                icon = "⏭️"
            elif status in ['dry_run_ok', 'published']:
                icon = "✅"
            else:
                icon = "❌"
            print(f"   {icon} {platform.capitalize()}: {status}")
    
    # Overall status
    creds_ok = sum(1 for status in credential_results.values() if status == 'credentials_ok')
    total_platforms = len(credential_results)
    
    print(f"\n📈 Overall Status: {creds_ok}/{total_platforms} platforms configured")
    
    if creds_ok == 0:
        print("\n⚠️  No platforms configured. See docs/api-setup.md for setup instructions.")
    elif creds_ok < total_platforms:
        print(f"\n⚠️  {total_platforms - creds_ok} platform(s) need configuration.")
        print("   See docs/api-setup.md for setup instructions.")
    else:
        print("\n🎉 All platforms configured! You're ready to start publishing.")
    
    print("\n💡 Next Steps:")
    if creds_ok > 0:
        print("   1. Create your first real blog post in _posts/")
        print("   2. Configure social_media settings in the post front matter")
        print("   3. Push to GitHub to trigger automated publishing")
        print("   4. Monitor the GitHub Actions workflow")
    else:
        print("   1. Set up API credentials (see docs/api-setup.md)")
        print("   2. Run this test script again to verify setup")
        print("   3. Start creating content!")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Auto Publisher Blog integrations')
    parser.add_argument('--platforms', nargs='+', 
                       choices=['linkedin', 'medium', 'reddit', 'twitter'],
                       help='Platforms to test (default: all)')
    parser.add_argument('--live', action='store_true',
                       help='Publish actual test posts (default: dry run)')
    parser.add_argument('--credentials-only', action='store_true',
                       help='Only test credentials, skip publishing test')
    
    args = parser.parse_args()
    
    print("🤖 Auto Publisher Blog - Integration Tester")
    print("=" * 50)
    
    # Test credentials
    credential_results = test_credentials()
    
    # Test publishing if requested
    publishing_results = None
    if not args.credentials_only:
        platforms = args.platforms or ['linkedin', 'medium', 'reddit', 'twitter']
        publishing_results = test_publishing(platforms, dry_run=not args.live)
    
    # Print summary
    print_summary(credential_results, publishing_results)

if __name__ == "__main__":
    main()

