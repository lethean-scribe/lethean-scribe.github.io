# Auto Publisher Blog

🚀 **Write once, publish everywhere.** A Jekyll blog with automated cross-platform publishing to LinkedIn, Medium, Reddit, and X (Twitter).

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue?logo=github)](https://pages.github.com/)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-red?logo=jekyll)](https://jekyllrb.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?logo=github-actions)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **🔄 Automated Publishing**: Automatically share new blog posts to multiple social media platforms
- **📝 Jekyll-Powered**: Beautiful, fast-loading static blog with Markdown support
- **🎯 Smart Formatting**: Content automatically adapted for each platform's requirements
- **⚙️ Flexible Configuration**: Control which posts go where with per-post settings
- **🔒 Secure**: API credentials stored safely as GitHub Secrets
- **📊 Built-in Analytics**: Track publishing success and engagement
- **🎨 Responsive Design**: Mobile-friendly blog with modern styling
- **🆓 Free Hosting**: Powered by GitHub Pages at no cost

## 🌐 Supported Platforms

| Platform | Features | Content Type |
|----------|----------|--------------|
| **LinkedIn** | Professional networking, company pages | Articles, updates, professional content |
| **Medium** | Long-form publishing, publications | In-depth articles, tutorials, thought leadership |
| **Reddit** | Community engagement, subreddit targeting | Discussion starters, technical content |
| **X (Twitter)** | Real-time updates, hashtag optimization | Quick updates, announcements, threads |

## 🚀 Quick Start

### 1. Fork This Repository

Click the **"Fork"** button at the top of this page to create your own copy.

### 2. Enable GitHub Pages

1. Go to your forked repository's **Settings**
2. Navigate to **Pages** in the left sidebar
3. Under **Source**, select **"Deploy from a branch"**
4. Choose **main** branch and **/ (root)** folder
5. Click **Save**

Your blog will be available at `https://yourusername.github.io/auto-publisher-blog`

### 3. Configure API Credentials

Set up your social media API credentials following our [detailed setup guide](docs/api-setup.md).

### 4. Create Your First Post

Create a new file in the `_posts` directory with the format `YYYY-MM-DD-your-post-title.md`:

```markdown
---
layout: post
title: "Your Amazing Post Title"
date: 2025-09-23 10:00:00 +0000
categories: [blogging, automation]
tags: [jekyll, social-media]
excerpt: "A compelling summary of your post that will appear on social media."
social_media:
  linkedin: true
  medium: true
  reddit: 
    enabled: true
    subreddit: "programming"
  twitter: 
    enabled: true
    hashtags: ["#blogging", "#automation"]
---

Your amazing content goes here!
```

### 5. Push and Publish

Commit your new post and push to GitHub. The automation will automatically:

1. Detect your new post
2. Format it for each enabled platform
3. Publish to your configured social media accounts
4. Log the results for monitoring

## 📖 Documentation

- **[API Setup Guide](docs/api-setup.md)** - Step-by-step instructions for configuring each platform
- **[Configuration Reference](docs/configuration.md)** - Detailed configuration options
- **[Troubleshooting Guide](docs/troubleshooting.md)** - Common issues and solutions
- **[Advanced Features](docs/advanced.md)** - Power user features and customizations

## 🛠️ Local Development

### Prerequisites

- Python 3.8+
- Git
- Text editor

### Setup

1. **Clone your forked repository:**
   ```bash
   git clone https://github.com/yourusername/auto-publisher-blog.git
   cd auto-publisher-blog
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

4. **Configure your credentials in `.env`** (see [API Setup Guide](docs/api-setup.md))

5. **Test your integration:**
   ```bash
   python scripts/test_integration.py --credentials-only
   ```

### Testing

Run the integration tester to verify your setup:

```bash
# Test credentials only
python scripts/test_integration.py --credentials-only

# Dry run (no actual posts)
python scripts/test_integration.py

# Live test (publishes real test posts)
python scripts/test_integration.py --live

# Test specific platforms
python scripts/test_integration.py --platforms linkedin twitter
```

## ⚙️ Configuration

### Blog Configuration

Edit `_config.yml` to customize your blog:

```yaml
title: Your Blog Name
description: Your blog description
url: "https://yourusername.github.io/auto-publisher-blog"

# Social media automation settings
social:
  linkedin:
    enabled: true
  medium:
    enabled: true
  reddit:
    enabled: true
    subreddit: "programming"  # default subreddit
  twitter:
    enabled: true
    include_hashtags: true
```

### Per-Post Configuration

Control publishing for individual posts using front matter:

```yaml
social_media:
  linkedin: true                    # Simple enable/disable
  medium: true
  reddit: 
    enabled: true
    subreddit: "webdev"            # Override default subreddit
  twitter: 
    enabled: true
    hashtags: ["#coding", "#tips"]  # Custom hashtags
```

## 🔧 GitHub Actions Workflow

The automation runs on GitHub Actions with the following triggers:

- **Push to main branch** with changes in `_posts/`
- **Manual trigger** via GitHub Actions UI
- **Scheduled runs** (optional, configure in workflow file)

### Workflow Steps

1. **Detect Changes**: Identifies new or modified posts
2. **Parse Content**: Extracts title, excerpt, tags, and social media settings
3. **Parallel Publishing**: Publishes to all enabled platforms simultaneously
4. **Rate Limiting**: Respects API limits to avoid account suspension
5. **Error Handling**: Retries failed requests and logs detailed results
6. **Notification**: Reports success/failure status

## 🔒 Security & Privacy

### Credential Management

- **GitHub Secrets**: All API credentials stored as encrypted repository secrets
- **No Hardcoding**: Never commit credentials to your repository
- **Minimal Permissions**: Use least-privilege API access
- **Regular Rotation**: Rotate tokens and passwords regularly

### Best Practices

- Use dedicated social media accounts for automation when possible
- Monitor API usage to detect unauthorized access
- Review and audit published content regularly
- Keep dependencies updated for security patches

## 📊 Analytics & Monitoring

### Built-in Monitoring

- **Publishing Logs**: Detailed success/failure tracking in GitHub Actions
- **Rate Limit Monitoring**: Automatic rate limit compliance
- **Error Reporting**: Comprehensive error logging and retry logic

### External Analytics

Integrate with your preferred analytics tools:

- **Google Analytics**: Track blog traffic and engagement
- **Social Media Analytics**: Monitor platform-specific performance
- **Custom Dashboards**: Build dashboards using GitHub Actions logs

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Found an issue? [Open an issue](https://github.com/yourusername/auto-publisher-blog/issues)
- 💡 **Suggest Features**: Have an idea? [Start a discussion](https://github.com/yourusername/auto-publisher-blog/discussions)
- 📖 **Improve Documentation**: Help make our guides clearer
- 🔧 **Submit Code**: Fix bugs or add features via pull requests

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit with clear messages: `git commit -m 'Add amazing feature'`
5. Push to your branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Code Standards

- Follow PEP 8 for Python code
- Add docstrings to all functions and classes
- Include tests for new features
- Update documentation for any changes

## 📋 Roadmap

### Upcoming Features

- [ ] **Additional Platforms**: Instagram, TikTok, YouTube Community posts
- [ ] **Content Scheduling**: Delayed publishing and optimal timing
- [ ] **A/B Testing**: Test different content variations
- [ ] **Analytics Dashboard**: Built-in performance tracking
- [ ] **Content Templates**: Reusable post templates
- [ ] **Webhook Integration**: Real-time notifications
- [ ] **Multi-language Support**: Internationalization features

### Version History

- **v1.0.0** - Initial release with core automation features
- **v1.1.0** - Enhanced error handling and rate limiting
- **v1.2.0** - Added Reddit and improved Twitter integration
- **v2.0.0** - Complete rewrite with modular architecture

## ❓ FAQ

### General Questions

**Q: Is this free to use?**
A: Yes! The blog hosting (GitHub Pages) and automation (GitHub Actions) are free for public repositories.

**Q: Do I need coding experience?**
A: Basic familiarity with Git and Markdown is helpful, but detailed guides are provided for all setup steps.

**Q: Can I customize the blog design?**
A: Absolutely! The Jekyll theme is fully customizable. Edit the CSS, layouts, and templates as needed.

### Technical Questions

**Q: What happens if an API is down?**
A: The system includes retry logic and will attempt to publish again. Failed posts are logged for manual review.

**Q: Can I publish to only some platforms?**
A: Yes! Use the `social_media` configuration in each post's front matter to control which platforms receive the content.

**Q: How do I handle rate limits?**
A: Built-in rate limiting automatically manages API calls to stay within platform limits.

### Troubleshooting

**Q: My posts aren't being published automatically.**
A: Check the GitHub Actions logs for errors. Common issues include invalid API credentials or incorrect post formatting.

**Q: I'm getting authentication errors.**
A: Verify your API credentials are correctly configured in GitHub Secrets and haven't expired.

For more help, see our [Troubleshooting Guide](docs/troubleshooting.md) or [open an issue](https://github.com/yourusername/auto-publisher-blog/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Jekyll Team** - For the amazing static site generator
- **GitHub** - For free hosting and automation via GitHub Pages and Actions
- **Social Media APIs** - For enabling automated publishing
- **Open Source Community** - For inspiration and contributions

## 📞 Support

- 📖 **Documentation**: Check our comprehensive guides in the `docs/` folder
- 💬 **Discussions**: Join conversations in [GitHub Discussions](https://github.com/yourusername/auto-publisher-blog/discussions)
- 🐛 **Issues**: Report bugs via [GitHub Issues](https://github.com/yourusername/auto-publisher-blog/issues)
- 📧 **Email**: For private inquiries, contact [your-email@example.com](mailto:your-email@example.com)

---

**Ready to automate your content distribution?** [Get started now →](docs/api-setup.md)

*Made with ❤️ by the Auto Publisher Blog community*

