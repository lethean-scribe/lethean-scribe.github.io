#!/bin/bash

# Auto Publisher Blog Setup Script
# This script helps you set up your auto-publishing blog quickly

set -e

echo "🚀 Auto Publisher Blog Setup"
echo "=============================="
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "_config.yml" ] || [ ! -d "_posts" ]; then
    print_error "This doesn't appear to be an Auto Publisher Blog directory."
    print_info "Please run this script from the root of your forked repository."
    exit 1
fi

echo "🔍 Checking prerequisites..."

# Check Python
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version | cut -d' ' -f2)
    print_success "Python found (version $PYTHON_VERSION)"
else
    print_error "Python 3 is required but not found."
    print_info "Please install Python 3.8 or later and try again."
    exit 1
fi

# Check pip
if command -v pip3 &> /dev/null; then
    print_success "pip3 found"
else
    print_error "pip3 is required but not found."
    exit 1
fi

# Check git
if command -v git &> /dev/null; then
    print_success "Git found"
else
    print_error "Git is required but not found."
    exit 1
fi

echo
echo "📦 Installing Python dependencies..."

# Install Python dependencies
if pip3 install -r requirements.txt; then
    print_success "Python dependencies installed"
else
    print_error "Failed to install Python dependencies"
    exit 1
fi

echo
echo "⚙️  Setting up configuration..."

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
    print_success "Created .env file from template"
    print_warning "Please edit .env file with your API credentials"
else
    print_info ".env file already exists"
fi

# Get user information for configuration
echo
echo "📝 Let's configure your blog..."

read -p "Enter your blog title: " BLOG_TITLE
read -p "Enter your name/author: " AUTHOR_NAME
read -p "Enter your email: " AUTHOR_EMAIL
read -p "Enter your GitHub username: " GITHUB_USERNAME
read -p "Enter your repository name (default: auto-publisher-blog): " REPO_NAME

# Set defaults
REPO_NAME=${REPO_NAME:-auto-publisher-blog}
SITE_URL="https://${GITHUB_USERNAME}.github.io/${REPO_NAME}"

# Update _config.yml
echo "Updating _config.yml..."
sed -i.bak "s/title: Auto Publisher Blog/title: ${BLOG_TITLE}/" _config.yml
sed -i.bak "s/email: your-email@example.com/email: ${AUTHOR_EMAIL}/" _config.yml
sed -i.bak "s/yourusername/${GITHUB_USERNAME}/g" _config.yml
sed -i.bak "s/auto-publisher-blog/${REPO_NAME}/g" _config.yml

# Update .env file
sed -i.bak "s/yourusername/${GITHUB_USERNAME}/g" .env
sed -i.bak "s/auto-publisher-blog/${REPO_NAME}/g" .env

print_success "Configuration updated"

echo
echo "🧪 Testing setup..."

# Test the integration
if python3 scripts/test_integration.py --credentials-only; then
    print_success "Setup test completed"
else
    print_warning "Some issues detected - check the output above"
fi

echo
echo "🎉 Setup Complete!"
echo "=================="
echo
print_info "Next steps:"
echo "1. Edit your .env file with API credentials (see docs/api-setup.md)"
echo "2. Add the same credentials to GitHub Secrets in your repository"
echo "3. Create your first blog post in the _posts/ directory"
echo "4. Push to GitHub to trigger automated publishing"
echo
print_info "Useful commands:"
echo "• Test credentials: python3 scripts/test_integration.py --credentials-only"
echo "• Test publishing: python3 scripts/test_integration.py"
echo "• Create new post: cp _posts/2025-09-23-welcome-to-auto-publisher.md _posts/$(date +%Y-%m-%d)-my-new-post.md"
echo
print_info "Documentation:"
echo "• API Setup: docs/api-setup.md"
echo "• Full README: README.md"
echo "• GitHub repository: https://github.com/${GITHUB_USERNAME}/${REPO_NAME}"
echo
print_success "Happy blogging! 🚀"

