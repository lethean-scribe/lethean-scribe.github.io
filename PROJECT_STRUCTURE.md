# Project Structure

This document explains the organization and purpose of files in the Auto Publisher Blog project.

## 📁 Directory Structure

```
auto-publisher-blog/
├── 📄 README.md                    # Main project documentation
├── 📄 LICENSE                      # MIT license
├── 📄 setup.sh                     # Quick setup script
├── 📄 requirements.txt              # Python dependencies
├── 📄 Gemfile                       # Ruby/Jekyll dependencies
├── 📄 _config.yml                   # Jekyll configuration
├── 📄 index.md                      # Homepage content
├── 📄 about.md                      # About page
├── 📄 .env.example                  # Environment variables template
├── 📄 .gitignore                    # Git ignore rules
├── 📄 PROJECT_STRUCTURE.md          # This file
│
├── 📁 _posts/                       # Blog posts directory
│   ├── 📄 2025-09-23-welcome-to-auto-publisher.md
│   └── 📄 2025-09-23-github-actions-social-media-automation.md
│
├── 📁 _layouts/                     # Jekyll page templates
│   ├── 📄 default.html             # Base layout template
│   └── 📄 post.html                # Blog post template
│
├── 📁 _includes/                    # Reusable template components
│   ├── 📄 head.html                # HTML head section
│   ├── 📄 header.html              # Site header/navigation
│   └── 📄 footer.html              # Site footer
│
├── 📁 assets/                       # Static assets
│   └── 📁 css/
│       └── 📄 style.scss            # Custom CSS styles
│
├── 📁 scripts/                      # Automation scripts
│   ├── 📄 social_publisher.py      # Main publishing logic
│   └── 📄 test_integration.py      # Integration testing
│
├── 📁 docs/                         # Documentation
│   └── 📄 api-setup.md             # API setup guide
│
└── 📁 .github/                      # GitHub-specific files
    └── 📁 workflows/
        └── 📄 publish-to-social.yml # GitHub Actions workflow
```

## 📄 File Descriptions

### Core Configuration

- **`_config.yml`** - Jekyll site configuration including social media settings
- **`requirements.txt`** - Python packages needed for automation
- **`Gemfile`** - Ruby gems for Jekyll (GitHub Pages compatible)
- **`.env.example`** - Template for local environment variables
- **`.gitignore`** - Prevents sensitive files from being committed

### Content Files

- **`index.md`** - Homepage with feature overview and recent posts
- **`about.md`** - About page explaining the project
- **`_posts/*.md`** - Individual blog posts with front matter configuration

### Jekyll Templates

- **`_layouts/default.html`** - Base HTML structure for all pages
- **`_layouts/post.html`** - Template specifically for blog posts
- **`_includes/head.html`** - HTML head section with meta tags
- **`_includes/header.html`** - Site navigation and branding
- **`_includes/footer.html`** - Site footer with links and info

### Automation System

- **`scripts/social_publisher.py`** - Core publishing logic for all platforms
- **`scripts/test_integration.py`** - Testing script for API credentials
- **`.github/workflows/publish-to-social.yml`** - GitHub Actions automation

### Documentation

- **`README.md`** - Main project documentation and setup guide
- **`docs/api-setup.md`** - Detailed API credential setup instructions
- **`PROJECT_STRUCTURE.md`** - This file explaining project organization

### Utilities

- **`setup.sh`** - Interactive setup script for quick configuration
- **`LICENSE`** - MIT license for open source distribution

## 🔧 Key Components

### 1. Jekyll Blog Engine

The blog is built on Jekyll, a static site generator that converts Markdown files into a beautiful website:

- **Posts**: Written in Markdown with YAML front matter
- **Layouts**: HTML templates that define page structure
- **Includes**: Reusable components for consistent design
- **Assets**: CSS, JavaScript, and images for styling

### 2. GitHub Actions Automation

The automation system uses GitHub Actions to:

- **Detect**: New or modified posts when you push to GitHub
- **Parse**: Extract content and social media configuration
- **Publish**: Automatically post to configured platforms
- **Monitor**: Log results and handle errors gracefully

### 3. Social Media Integration

Platform-specific publishers handle the unique requirements of each service:

- **LinkedIn**: Professional networking posts with proper formatting
- **Medium**: Long-form articles with HTML conversion
- **Reddit**: Community posts with subreddit targeting
- **Twitter**: Short-form updates with hashtag optimization

### 4. Configuration System

Flexible configuration at multiple levels:

- **Global**: Site-wide settings in `_config.yml`
- **Per-post**: Individual post settings in front matter
- **Environment**: API credentials and local settings

## 🚀 Workflow Overview

### Content Creation Workflow

1. **Write**: Create new post in `_posts/` directory
2. **Configure**: Set social media options in front matter
3. **Commit**: Push changes to GitHub repository
4. **Automate**: GitHub Actions detects changes and publishes
5. **Monitor**: Check workflow logs for publishing status

### Development Workflow

1. **Setup**: Run `./setup.sh` for initial configuration
2. **Test**: Use `scripts/test_integration.py` to verify API setup
3. **Develop**: Make changes to templates, styles, or automation
4. **Deploy**: Push to GitHub for automatic deployment

### Maintenance Workflow

1. **Monitor**: Check GitHub Actions logs regularly
2. **Update**: Keep dependencies and API credentials current
3. **Optimize**: Analyze performance and adjust settings
4. **Backup**: Ensure content and configuration are backed up

## 🔒 Security Considerations

### Sensitive Files

These files should NEVER be committed to your repository:

- **`.env`** - Contains API credentials (use `.env.example` as template)
- **`*.log`** - May contain sensitive information
- **`temp_*`** - Temporary files that might contain credentials

### GitHub Secrets

Store all API credentials as GitHub repository secrets:

- Navigate to repository Settings > Secrets and variables > Actions
- Add each credential as a separate secret
- Reference in workflows using `${{ secrets.SECRET_NAME }}`

### Best Practices

- **Rotate credentials** regularly
- **Use minimal permissions** for API access
- **Monitor usage** for unauthorized access
- **Keep dependencies updated** for security patches

## 📈 Customization Guide

### Adding New Platforms

To add support for a new social media platform:

1. **Create publisher class** in `scripts/social_publisher.py`
2. **Add platform configuration** to `_config.yml`
3. **Update workflow** in `.github/workflows/publish-to-social.yml`
4. **Add documentation** to `docs/api-setup.md`
5. **Test integration** with `scripts/test_integration.py`

### Modifying Design

To customize the blog appearance:

1. **Edit CSS** in `assets/css/style.scss`
2. **Modify layouts** in `_layouts/` directory
3. **Update includes** in `_includes/` directory
4. **Add assets** to `assets/` directory

### Extending Automation

To add new automation features:

1. **Modify workflow** in `.github/workflows/publish-to-social.yml`
2. **Update publisher logic** in `scripts/social_publisher.py`
3. **Add configuration options** to `_config.yml`
4. **Update documentation** accordingly

## 🆘 Troubleshooting

### Common Issues

- **Posts not publishing**: Check GitHub Actions logs for errors
- **Authentication failures**: Verify API credentials in GitHub Secrets
- **Build failures**: Ensure Jekyll configuration is valid
- **Missing dependencies**: Run `pip install -r requirements.txt`

### Debug Mode

Enable debug logging by setting environment variables:

```bash
export DEBUG=true
export LOG_LEVEL=DEBUG
python scripts/test_integration.py
```

### Getting Help

1. **Check documentation** in `docs/` directory
2. **Review GitHub Actions logs** for error details
3. **Test locally** using provided scripts
4. **Open an issue** on GitHub for persistent problems

---

This structure provides a solid foundation for automated content publishing while remaining flexible and extensible for future enhancements.

