---
layout: default
title: Home
---

<div class="home">

  <h1 class="page-heading">Auto Publisher Blog</h1>
  
  <p class="lead">Write once, publish everywhere. This Jekyll blog automatically shares your content to LinkedIn, Medium, Reddit, and X (Twitter).</p>

  <div class="features">
    <div class="feature">
      <h3>🚀 Automated Publishing</h3>
      <p>New posts are automatically shared to all connected social media platforms using GitHub Actions.</p>
    </div>
    
    <div class="feature">
      <h3>🎯 Smart Formatting</h3>
      <p>Content is automatically adapted for each platform's requirements and audience expectations.</p>
    </div>
    
    <div class="feature">
      <h3>⚙️ Customizable Rules</h3>
      <p>Control which posts go where with flexible per-post configuration options.</p>
    </div>
    
    <div class="feature">
      <h3>📊 Built-in Analytics</h3>
      <p>Track performance across all platforms with integrated monitoring and reporting.</p>
    </div>
  </div>

  <h2>Recent Posts</h2>

  {%- if site.posts.size > 0 -%}
    <ul class="post-list">
      {%- for post in site.posts limit: 5 -%}
      <li>
        {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        {%- if site.show_excerpts -%}
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
        {%- endif -%}
        
        <div class="post-tags">
          {%- for tag in post.tags -%}
            <span class="tag">{{ tag }}</span>
          {%- endfor -%}
        </div>
      </li>
      {%- endfor -%}
    </ul>

    <p class="rss-subscribe">Subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a> to get updates automatically.</p>
  {%- endif -%}

  <div class="getting-started">
    <h2>Get Started</h2>
    <p>Ready to set up your own auto-publishing blog? Here's how:</p>
    <ol>
      <li><strong>Fork this repository</strong> to your GitHub account</li>
      <li><strong>Configure your API credentials</strong> in GitHub Secrets</li>
      <li><strong>Customize the settings</strong> in <code>_config.yml</code></li>
      <li><strong>Start writing</strong> and watch your content spread automatically!</li>
    </ol>
    
    <p><a href="https://github.com/yourusername/auto-publisher-blog" class="btn">View on GitHub</a></p>
  </div>

</div>

