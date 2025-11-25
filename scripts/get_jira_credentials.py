#!/usr/bin/env python3
"""
Helper script to retrieve Jira credentials from macOS Keychain
"""

import subprocess
import sys

def get_keychain_password(service_name):
    """Retrieve password from macOS Keychain."""
    try:
        result = subprocess.run(
            ['security', 'find-generic-password', '-s', service_name, '-w'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_jira_credentials():
    """Get all Jira credentials from Keychain."""
    email = get_keychain_password('jira-email')
    pat = get_keychain_password('jira-pat')
    org = get_keychain_password('jira-organization')
    
    return {
        'email': email,
        'pat': pat,
        'organization': org
    }

def main():
    """Main function to display or export credentials."""
    creds = get_jira_credentials()
    
    if not all(creds.values()):
        print("❌ Error: Jira credentials not found in Keychain", file=sys.stderr)
        print("Run setup_jira_credentials.sh first to store them", file=sys.stderr)
        sys.exit(1)
    
    # Check if we should export as environment variables
    if '--export' in sys.argv:
        print(f"export JIRA_EMAIL='{creds['email']}'")
        print(f"export JIRA_PAT='{creds['pat']}'")
        print(f"export JIRA_ORG='{creds['organization']}'")
    else:
        print("✅ Jira Credentials Found:")
        print(f"   Email: {creds['email']}")
        print(f"   PAT: {'*' * len(creds['pat'])} (hidden)")
        print(f"   Organization: {creds['organization']}")
        print()
        print("To use in scripts:")
        print("  from get_jira_credentials import get_jira_credentials")
        print("  creds = get_jira_credentials()")
        print()
        print("To export as environment variables:")
        print("  eval $(python3 scripts/get_jira_credentials.py --export)")

if __name__ == '__main__':
    main()
