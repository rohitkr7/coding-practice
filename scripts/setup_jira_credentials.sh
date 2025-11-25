#!/bin/bash
# Setup script to store Jira credentials in macOS Keychain

echo "🔐 Jira Credentials Setup"
echo "=========================="
echo ""
echo "This script will securely store your Jira credentials in macOS Keychain."
echo ""

# Prompt for Jira email
read -p "Enter your Jira email: " JIRA_EMAIL

# Prompt for Jira PAT (hidden input)
read -sp "Enter your Jira Personal Access Token (PAT): " JIRA_PAT
echo ""

# Prompt for Jira organization
read -p "Enter your Jira organization (e.g., rohitroy007): " JIRA_ORG

echo ""
echo "Storing credentials in macOS Keychain..."

# Store Jira email
security add-generic-password \
    -a "$USER" \
    -s "jira-email" \
    -w "$JIRA_EMAIL" \
    -U 2>/dev/null || \
security delete-generic-password -s "jira-email" 2>/dev/null && \
security add-generic-password \
    -a "$USER" \
    -s "jira-email" \
    -w "$JIRA_EMAIL"

# Store Jira PAT
security add-generic-password \
    -a "$USER" \
    -s "jira-pat" \
    -w "$JIRA_PAT" \
    -U 2>/dev/null || \
security delete-generic-password -s "jira-pat" 2>/dev/null && \
security add-generic-password \
    -a "$USER" \
    -s "jira-pat" \
    -w "$JIRA_PAT"

# Store Jira organization
security add-generic-password \
    -a "$USER" \
    -s "jira-organization" \
    -w "$JIRA_ORG" \
    -U 2>/dev/null || \
security delete-generic-password -s "jira-organization" 2>/dev/null && \
security add-generic-password \
    -a "$USER" \
    -s "jira-organization" \
    -w "$JIRA_ORG"

echo ""
echo "✅ Credentials stored successfully in macOS Keychain!"
echo ""
echo "You can now retrieve them in your scripts using:"
echo "  security find-generic-password -s 'jira-email' -w"
echo "  security find-generic-password -s 'jira-pat' -w"
echo "  security find-generic-password -s 'jira-organization' -w"
echo ""
