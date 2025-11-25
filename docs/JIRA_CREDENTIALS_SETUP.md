# 🔐 Jira Credentials Setup Guide

This guide explains how to securely store and use your Jira credentials using macOS Keychain.

---

## 🎯 Why Use Keychain?

- **Secure**: Encrypted storage, not plain text
- **Convenient**: Scripts can auto-retrieve credentials
- **Safe**: Won't accidentally commit secrets to Git
- **Standard**: macOS recommended practice

---

## 📝 Setup Instructions

### Step 1: Store Your Credentials

Run the setup script:

```bash
./scripts/setup_jira_credentials.sh
```

You'll be prompted for:
- **Jira Email**: Your Atlassian account email
- **Jira PAT**: Your Personal Access Token (input is hidden)
- **Jira Organization**: Your organization name (e.g., `rohitroy007`)

### Step 2: Verify Storage

Check that credentials were stored:

```bash
python3 scripts/get_jira_credentials.py
```

You should see:
```
✅ Jira Credentials Found:
   Email: your-email@example.com
   PAT: ************************ (hidden)
   Organization: rohitroy007
```

---

## 🔧 Using Credentials in Scripts

### Option 1: Python Import

```python
from scripts.get_jira_credentials import get_jira_credentials

creds = get_jira_credentials()
email = creds['email']
pat = creds['pat']
org = creds['organization']
```

### Option 2: Environment Variables

```bash
# Export to current shell
eval $(python3 scripts/get_jira_credentials.py --export)

# Now use them
echo $JIRA_EMAIL
echo $JIRA_PAT
echo $JIRA_ORG
```

### Option 3: Direct Shell Command

```bash
# Get individual values
JIRA_PAT=$(security find-generic-password -s 'jira-pat' -w)
JIRA_EMAIL=$(security find-generic-password -s 'jira-email' -w)
JIRA_ORG=$(security find-generic-password -s 'jira-organization' -w)
```

---

## 🔄 Update Credentials

To update your credentials, simply run the setup script again:

```bash
./scripts/setup_jira_credentials.sh
```

It will overwrite the existing credentials.

---

## 🗑️ Delete Credentials

To remove credentials from Keychain:

```bash
security delete-generic-password -s 'jira-email'
security delete-generic-password -s 'jira-pat'
security delete-generic-password -s 'jira-organization'
```

---

## 🔗 Getting Your Jira PAT

If you don't have a Personal Access Token yet:

1. Go to: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**
3. Give it a name (e.g., "LeetCode Practice")
4. Copy the token (you won't see it again!)
5. Use it in the setup script

---

## 🛡️ Security Notes

- ✅ Credentials are encrypted in macOS Keychain
- ✅ Never commit `.env` files or hardcoded tokens to Git
- ✅ Keychain requires your Mac password to access
- ✅ Scripts can only access credentials you've stored
- ⚠️ Don't share your PAT with anyone
- ⚠️ Rotate your PAT periodically for security

---

## 📚 Example: Using in process_jira_items.py

Update your `process_jira_items.py` to use Keychain:

```python
from get_jira_credentials import get_jira_credentials

# Get credentials from Keychain
creds = get_jira_credentials()

# Use in Jira API calls
headers = {
    'Authorization': f'Bearer {creds["pat"]}',
    'Content-Type': 'application/json'
}

jira_url = f'https://{creds["organization"]}.atlassian.net/rest/api/3/...'
```

---

## ✅ Benefits Summary

| Method | Security | Convenience | Git-Safe |
|--------|----------|-------------|----------|
| Hardcoded | ❌ Low | ✅ Easy | ❌ No |
| .env file | ⚠️ Medium | ✅ Easy | ⚠️ If .gitignore |
| **Keychain** | ✅ **High** | ✅ **Easy** | ✅ **Yes** |

---

**Recommended**: Always use Keychain for sensitive credentials! 🔐
