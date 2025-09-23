---
layout: post
title: "Automation Instructions for Cross-Platform Publishing"
date: 2025-09-23 10:00:00 -0500
categories: [CFD, Aerodynamics, Tutorials]
tags: [airfoil, simulation, fluid dynamics, NACA, OpenFOAM, ANSYS Fluent]
author: "HyperSocks"
---

## Automation Instructions for Cross-Platform Publishing

This document outlines how to set up automation workflows using services like Zapier or IFTTT to automatically publish your CFD content from your Jekyll-based GitHub Pages site to other platforms.

**Prerequisites:**
1.  Your Jekyll site is deployed on GitHub Pages and accessible via `https://your-username.github.io`.
2.  Your Jekyll site has an RSS feed (usually at `https://your-username.github.io/feed.xml`).
3.  You have accounts on Zapier (or IFTTT/Make.com), Medium, LinkedIn, and Twitter.

### Step 1: Find Your RSS Feed URL

Your Jekyll site automatically generates an RSS feed. Typically, this will be located at:

`https://your-username.github.io/feed.xml`

Replace `your-username` with your actual GitHub username. This URL will be the 'trigger' for all your automation workflows.

### Step 2: Set up Zapier (or IFTTT/Make.com) Workflows

#### Workflow 1: Auto-post to Medium

**Goal:** When a new post is published on your Jekyll site, automatically create a new story on Medium.

1.  **Create a new Zap/Applet/Scenario:**
2.  **Trigger:** Search for "RSS by Zapier" (or similar for IFTTT). Select "New Item in Feed."
3.  **Feed URL:** Enter your Jekyll site's RSS feed URL (e.g., `https://your-username.github.io/feed.xml`).
4.  **Action:** Search for "Medium." Select "Create Story."
5.  **Connect your Medium account.**
6.  **Customize Story:**
    *   **Title:** Use the "Title" field from your RSS feed.
    *   **Content:** Use the "Content" or "Description" field from your RSS feed. (Note: Medium might strip some HTML/Markdown, so review the first few posts).
    *   **Canonical URL:** **Crucially, set this to the "Link" field from your RSS feed.** This tells Medium that your GitHub Pages site is the original source, which is good for SEO.
    *   **Tags:** You can manually add relevant tags (e.g., CFD, Engineering, Simulation) or try to extract them from your RSS feed if your Jekyll setup includes them.
    *   **Status:** Choose "Draft" or "Publish." Starting with "Draft" is recommended so you can review and format it on Medium before publishing.
7.  **Test and Activate your Zap/Applet/Scenario.**

#### Workflow 2: Share on LinkedIn

**Goal:** When a new post is published, share a link to it on your LinkedIn profile.

1.  **Create a new Zap/Applet/Scenario.**
2.  **Trigger:** "RSS by Zapier" -> "New Item in Feed." Use your Jekyll RSS feed URL.
3.  **Action:** Search for "LinkedIn." Select "Create Share Update."
4.  **Connect your LinkedIn account.**
5.  **Customize Share Update:**
    *   **Content:** Combine the "Title" and "Link" from your RSS feed. You can add a custom message like: "New CFD tutorial just dropped! Check out: [Title] [Link]".
    *   **Visibility:** Choose "Anyone" or "Connections."
6.  **Test and Activate.**

#### Workflow 3: Share on Twitter (X)

**Goal:** When a new post is published, tweet a link to it.

1.  **Create a new Zap/Applet/Scenario.**
2.  **Trigger:** "RSS by Zapier" -> "New Item in Feed." Use your Jekyll RSS feed URL.
3.  **Action:** Search for "Twitter." Select "Create Tweet."
4.  **Connect your Twitter account.**
5.  **Customize Tweet:**
    *   **Message:** Combine the "Title" and "Link" from your RSS feed. Add relevant hashtags (e.g., #CFD #Engineering #Simulation).
6.  **Test and Activate.**

#### Workflow 4: Notify for Reddit Posting (Manual/Semi-Automated)

**Goal:** Get a notification when a new post is ready, so you can manually post it to Reddit (to ensure compliance with subreddit rules and add personal context).

1.  **Create a new Zap/Applet/Scenario.**
2.  **Trigger:** "RSS by Zapier" -> "New Item in Feed." Use your Jekyll RSS feed URL.
3.  **Action:** Search for "Email" (e.g., Gmail, or Zapier's built-in email) or "Slack" or "Discord" (if you use these for notifications).
4.  **Customize Email/Message:**
    *   **Subject:** "New CFD Post Ready for Reddit: [Title]"
    *   **Body:** Include the "Title" and "Link" from your RSS feed, along with a reminder to check subreddit rules before posting.
5.  **Test and Activate.**

By following these steps, you can create a powerful and mostly automated content distribution pipeline, allowing you to focus on creating valuable CFD content.

