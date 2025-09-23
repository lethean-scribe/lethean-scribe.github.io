# Social Media API Setup Guide

This guide walks you through setting up API credentials for each social media platform supported by the Auto Publisher Blog.

## Overview

The automation system requires API credentials for each platform you want to publish to. These credentials are stored securely as GitHub Secrets and never exposed in your repository code.

### Required Credentials Summary

| Platform | Required Secrets | Optional Secrets |
|----------|------------------|------------------|
| LinkedIn | `LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_PERSON_ID` | - |
| Medium | `MEDIUM_ACCESS_TOKEN` | `MEDIUM_USER_ID` |
| Reddit | `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD` | - |
| Twitter/X | `TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET` | `TWITTER_BEARER_TOKEN` |

---

## LinkedIn API Setup

LinkedIn uses OAuth 2.0 for authentication. You'll need to create a LinkedIn app and obtain an access token.

### Step 1: Create a LinkedIn App

1. Go to the [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
2. Click **"Create App"**
3. Fill in the required information:
   - **App name**: Your blog name (e.g., "Auto Publisher Blog")
   - **LinkedIn Page**: Your personal LinkedIn profile or company page
   - **Privacy policy URL**: Your blog's privacy policy (can be a simple page)
   - **App logo**: Upload a logo (optional but recommended)
4. Click **"Create app"**

### Step 2: Configure App Permissions

1. In your app dashboard, go to the **"Products"** tab
2. Request access to **"Share on LinkedIn"** and **"Sign In with LinkedIn"**
3. Wait for approval (usually instant for personal use)

### Step 3: Get Your Credentials

1. Go to the **"Auth"** tab in your app dashboard
2. Note down your **Client ID** and **Client Secret**
3. Add your redirect URI: `https://localhost:8080/callback` (for testing)

### Step 4: Generate Access Token

You can use LinkedIn's OAuth 2.0 flow or use a tool like Postman. Here's a simple method:

1. Create an authorization URL:
   ```
   https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=https://localhost:8080/callback&scope=r_liteprofile%20w_member_social
   ```

2. Visit this URL in your browser and authorize the app
3. Copy the authorization code from the redirect URL
4. Exchange the code for an access token:

   ```bash
   curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     -d 'grant_type=authorization_code' \
     -d 'code=YOUR_AUTHORIZATION_CODE' \
     -d 'redirect_uri=https://localhost:8080/callback' \
     -d 'client_id=YOUR_CLIENT_ID' \
     -d 'client_secret=YOUR_CLIENT_SECRET'
   ```

### Step 5: Get Your Person ID

Use your access token to get your LinkedIn person ID:

```bash
curl -X GET https://api.linkedin.com/v2/people/~?projection=(id) \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

### Step 6: Add to GitHub Secrets

In your GitHub repository:
1. Go to **Settings > Secrets and variables > Actions**
2. Add these secrets:
   - `LINKEDIN_ACCESS_TOKEN`: Your access token
   - `LINKEDIN_PERSON_ID`: Your person ID (without the `urn:li:person:` prefix)

---

## Medium API Setup

Medium provides a simple integration token for publishing.

### Step 1: Get Your Integration Token

1. Go to [Medium Settings](https://medium.com/me/settings)
2. Scroll down to **"Integration tokens"**
3. Enter a description (e.g., "Auto Publisher Blog")
4. Click **"Get integration token"**
5. Copy the generated token

### Step 2: Get Your User ID (Optional)

The system can automatically fetch your user ID, but you can also get it manually:

```bash
curl -X GET https://api.medium.com/v1/me \
  -H 'Authorization: Bearer YOUR_INTEGRATION_TOKEN'
```

### Step 3: Add to GitHub Secrets

1. Go to **Settings > Secrets and variables > Actions**
2. Add these secrets:
   - `MEDIUM_ACCESS_TOKEN`: Your integration token
   - `MEDIUM_USER_ID`: Your user ID (optional)

---

## Reddit API Setup

Reddit uses OAuth 2.0 with client credentials and user authentication.

### Step 1: Create a Reddit App

1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Click **"Create App"** or **"Create Another App"**
3. Fill in the details:
   - **Name**: Your app name (e.g., "Auto Publisher Bot")
   - **App type**: Select **"script"**
   - **Description**: Brief description of your bot
   - **About URL**: Your blog URL (optional)
   - **Redirect URI**: `http://localhost:8080` (required but not used for script apps)
4. Click **"Create app"**

### Step 2: Get Your Credentials

After creating the app, you'll see:
- **Client ID**: The string under your app name (looks like `abc123def456`)
- **Client Secret**: The "secret" field

### Step 3: Add to GitHub Secrets

1. Go to **Settings > Secrets and variables > Actions**
2. Add these secrets:
   - `REDDIT_CLIENT_ID`: Your app's client ID
   - `REDDIT_CLIENT_SECRET`: Your app's client secret
   - `REDDIT_USERNAME`: Your Reddit username
   - `REDDIT_PASSWORD`: Your Reddit password

**Security Note**: Consider creating a dedicated Reddit account for your bot to avoid using your personal credentials.

---

## Twitter/X API Setup

Twitter requires approval for API access and uses OAuth 1.0a.

### Step 1: Apply for Twitter Developer Account

1. Go to the [Twitter Developer Portal](https://developer.twitter.com/)
2. Click **"Sign up"** and log in with your Twitter account
3. Apply for a developer account:
   - Choose **"Making a bot"** as your use case
   - Describe your automation project
   - Agree to the terms and submit your application
4. Wait for approval (can take a few days)

### Step 2: Create a Twitter App

1. Once approved, go to the [Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Click **"Create Project"** or **"Create App"**
3. Fill in your app details:
   - **App name**: Your bot name (e.g., "Auto Publisher Bot")
   - **Description**: What your bot does
   - **Website URL**: Your blog URL
4. Complete the setup

### Step 3: Generate API Keys

1. In your app dashboard, go to **"Keys and tokens"**
2. Generate/regenerate:
   - **API Key** and **API Key Secret**
   - **Access Token** and **Access Token Secret**
3. Make sure your app has **Read and Write** permissions

### Step 4: Add to GitHub Secrets

1. Go to **Settings > Secrets and variables > Actions**
2. Add these secrets:
   - `TWITTER_API_KEY`: Your API key
   - `TWITTER_API_SECRET`: Your API key secret
   - `TWITTER_ACCESS_TOKEN`: Your access token
   - `TWITTER_ACCESS_TOKEN_SECRET`: Your access token secret
   - `TWITTER_BEARER_TOKEN`: Your bearer token (optional)

---

## GitHub Secrets Configuration

### Adding Secrets to Your Repository

1. Go to your GitHub repository
2. Click **Settings** (in the repository, not your account)
3. In the left sidebar, click **Secrets and variables > Actions**
4. Click **"New repository secret"**
5. Enter the secret name and value
6. Click **"Add secret"**

### Environment Variables

You can also set a repository variable for your site URL:

1. In the same **Secrets and variables > Actions** page
2. Click the **"Variables"** tab
3. Click **"New repository variable"**
4. Add:
   - Name: `SITE_URL`
   - Value: `https://yourusername.github.io/your-repo-name`

### Security Best Practices

- **Never commit API credentials** to your repository
- **Use separate accounts** for bots when possible
- **Regularly rotate tokens** and credentials
- **Monitor API usage** to detect unauthorized access
- **Use minimal permissions** required for your use case

---

## Testing Your Setup

### Manual Testing

You can test individual platform integrations using the provided Python script:

```bash
# Install dependencies
pip install -r requirements.txt

# Test LinkedIn (example)
export LINKEDIN_ACCESS_TOKEN="your_token"
export LINKEDIN_PERSON_ID="your_person_id"
export SITE_URL="https://yourusername.github.io/repo"

python scripts/social_publisher.py linkedin '[{"title":"Test Post","excerpt":"This is a test","file_path":"_posts/2025-09-23-test.md","social_media":{"linkedin":true}}]'
```

### GitHub Actions Testing

1. Create a test post in `_posts/` with social media configuration
2. Push to your main branch
3. Check the **Actions** tab in your GitHub repository
4. Monitor the workflow execution and logs

### Troubleshooting Common Issues

#### LinkedIn Issues
- **403 Forbidden**: Check if your access token is valid and has the right permissions
- **400 Bad Request**: Verify your person ID format (should not include `urn:li:person:`)

#### Medium Issues
- **401 Unauthorized**: Check if your integration token is correct
- **400 Bad Request**: Ensure your content is properly formatted

#### Reddit Issues
- **403 Forbidden**: Verify your username/password and app credentials
- **429 Too Many Requests**: You're hitting rate limits, the system will automatically retry

#### Twitter Issues
- **401 Unauthorized**: Check all four credential values are correct
- **403 Forbidden**: Ensure your app has Read and Write permissions
- **429 Too Many Requests**: Rate limit exceeded, the system will wait and retry

---

## Rate Limits and Best Practices

Each platform has different rate limits:

- **LinkedIn**: 100 requests per hour per user
- **Medium**: 100 requests per hour per user  
- **Reddit**: 60 requests per hour per user
- **Twitter**: 300 requests per 15 minutes per user

The automation system includes built-in rate limiting to respect these limits and avoid getting your accounts suspended.

### Publishing Frequency Recommendations

- **Don't spam**: Space out your posts across platforms
- **Quality over quantity**: Focus on valuable content rather than frequent posting
- **Platform-appropriate timing**: Consider when your audience is most active on each platform
- **Monitor engagement**: Track which content performs best on which platforms

---

## Next Steps

Once you have all your API credentials configured:

1. **Test the integration** with a sample post
2. **Customize your automation settings** in `_config.yml`
3. **Create your first real post** with social media configuration
4. **Monitor the automation** through GitHub Actions logs
5. **Analyze performance** across platforms and adjust your strategy

For more advanced configuration options, see the [Advanced Configuration Guide](advanced-config.md).

