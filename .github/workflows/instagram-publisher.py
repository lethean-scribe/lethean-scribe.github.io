# .github/workflows/instagram-publisher.py
import requests
import feedparser
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_blog_post_image(title, summary):
    # Create a branded image for the blog post
    img = Image.new('RGB', (1080, 1080), color='white')
    draw = ImageDraw.Draw(img)
    
    # Add title and summary
    font_title = ImageFont.truetype('arial.ttf', 48)
    font_text = ImageFont.truetype('arial.ttf', 32)
    
    # Wrap text
    title_lines = textwrap.wrap(title, width=20)
    summary_lines = textwrap.wrap(summary, width=30)
    
    y_offset = 100
    for line in title_lines:
        draw.text((50, y_offset), line, font=font_title, fill='black')
        y_offset += 60
    
    y_offset += 50
    for line in summary_lines[:10]:  # Limit lines
        draw.text((50, y_offset), line, font=font_text, fill='gray')
        y_offset += 40
    
    img.save('blog_post.jpg')
    return 'blog_post.jpg'

def publish_to_instagram():
    access_token = os.environ['INSTAGRAM_ACCESS_TOKEN']
    instagram_account_id = os.environ['INSTAGRAM_ACCOUNT_ID']
    
    feed = feedparser.parse('https://lethean-scribe.github.io/feed.xml')
    
    for entry in feed.entries[:1]:
        # Create image
        image_path = create_blog_post_image(entry.title, entry.summary)
        
        # Upload image and create media object
        # (Implementation depends on your specific Instagram API setup)
        
        caption = f"{entry.title}\n\n{entry.summary[:200]}...\n\nRead more: {entry.link}\n\n#blog #tech #writing"
        
        # Post to Instagram (simplified - actual implementation more complex)
        media_data = {
            'image_url': image_path,  # You'd need to upload this first
            'caption': caption
        }