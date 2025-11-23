# Jira Integration Setup Guide

## Why Authentication is Needed

To fetch your Jira work items, we need to authenticate with your Atlassian account. This requires:
1. Your Atlassian email
2. A Jira API token (like a password, but more secure)

## Step-by-Step Setup

### Step 1: Create a Jira API Token

1. **Go to Atlassian Security Settings:**
   - Visit: https://id.atlassian.com/manage-profile/security/api-tokens
   - Log in with your Atlassian account

2. **Create API Token:**
   - Click the "Create API token" button
   - Give it a descriptive name: `Windsurf LnD Access`
   - Click "Create"

3. **Copy the Token:**
   - **IMPORTANT:** Copy the token immediately!
   - You won't be able to see it again
   - Store it safely (we'll use it in the next step)

### Step 2: Configure the Integration

#### Option A: Environment Variables (Recommended)

1. **Copy the template:**
   ```bash
   cp .env.template .env
   ```

2. **Edit the .env file:**
   ```bash
   # Open in your editor
   code .env  # or vim .env, nano .env, etc.
   ```

3. **Fill in your details:**
   ```
   JIRA_EMAIL=your-email@example.com
   JIRA_API_TOKEN=your-copied-token-here
   JIRA_HOST=https://rohitroy007.atlassian.net
   JIRA_PROJECT_KEY=LND
   JIRA_BOARD_ID=35
   ```

4. **Save the file**
   - The .env file is already in .gitignore, so it won't be committed to git

#### Option B: Manual Fetch (Alternative)

If the MCP integration doesn't work, we can fetch work items manually:

1. **Using Jira REST API directly:**
   ```bash
   # Set your credentials
   EMAIL="your-email@example.com"
   TOKEN="your-api-token"
   
   # Fetch issues assigned to you
   curl -u $EMAIL:$TOKEN \
     "https://rohitroy007.atlassian.net/rest/api/3/search?jql=project=LND+AND+assignee=currentUser()" \
     | jq '.' > jira-sync/work-items.json
   ```

2. **Or use the Jira web interface:**
   - Go to: https://rohitroy007.atlassian.net/jira/software/c/projects/LND/boards/35
   - Manually export your work items
   - Save to `jira-sync/work-items.json`

### Step 3: Test the Connection

Once configured, tell me:
```
"Fetch my Jira work items"
```

I'll attempt to connect and retrieve your issues.

## Troubleshooting

### Issue: "Authentication failed"
- **Check:** Email and token are correct
- **Check:** Token hasn't expired
- **Try:** Create a new API token

### Issue: "Project not found"
- **Check:** Project key is correct (LND)
- **Check:** You have access to the project
- **Check:** Board ID is correct (35)

### Issue: "No issues found"
- **Check:** Issues are actually assigned to you
- **Check:** JQL query is correct
- **Try:** View issues in web browser first

## Alternative: Manual Workflow

If automated fetching doesn't work, we can use a manual workflow:

1. **Export from Jira:**
   - Go to your board
   - Filter for your issues
   - Export as JSON or CSV

2. **Save to workspace:**
   - Place in `jira-sync/work-items.json`

3. **I'll read and process:**
   - I can read the file and help you organize problems
   - Create files in pattern folders
   - Track progress

## Security Notes

- ✅ API tokens are safer than passwords
- ✅ .env file is in .gitignore (won't be committed)
- ✅ Tokens can be revoked anytime
- ⚠️ Never share your API token
- ⚠️ Never commit .env to git
- ⚠️ Regenerate token if compromised

## What Happens After Setup

Once authenticated, I can:
1. ✅ Fetch all issues assigned to you
2. ✅ Read issue details (title, description, status)
3. ✅ Create problem files in appropriate pattern folders
4. ✅ Update issue status when you solve problems
5. ✅ Add comments with your solutions and learnings

## Need Help?

If you're stuck:
1. Check the Atlassian documentation: https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
2. Verify your Jira permissions
3. Try the manual workflow as a backup
4. Let me know what error you're seeing

---

**Ready?** Once you've created your API token, let me know and we'll test the connection!
