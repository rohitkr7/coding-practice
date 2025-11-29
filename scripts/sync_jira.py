#!/usr/bin/env python3
"""
Sync latest Jira data from the API.
"""

import json
import os
import subprocess
from pathlib import Path
from get_jira_credentials import get_jira_credentials

def fetch_jira_issues():
    """Fetch all issues from Jira using curl."""
    print("🔄 Fetching latest Jira data...")
    
    # Get credentials
    creds = get_jira_credentials()
    email = creds['email']
    api_token = creds['pat']  # PAT is the API token
    org = creds['organization']
    
    jira_host = f"https://{org}.atlassian.net"
    board_id = "35"  # Board ID from URL
    
    # Use board-specific endpoint to get issues from the board
    url = f"{jira_host}/rest/agile/1.0/board/{board_id}/issue"
    
    curl_cmd = [
        'curl', '-s',
        '-u', f'{email}:{api_token}',
        '-H', 'Accept: application/json',
        '-G', url,
        '--data-urlencode', 'maxResults=200',
        '--data-urlencode', 'fields=summary,status,description,labels,priority,created,updated,assignee',
        '--data-urlencode', 'jql=assignee=currentUser() ORDER BY status ASC, created DESC'
    ]
    
    try:
        result = subprocess.run(curl_cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        # Save to sync directory
        sync_dir = Path(__file__).parent.parent / 'jira' / 'sync'
        sync_dir.mkdir(parents=True, exist_ok=True)
        
        # Save detailed data
        output_file = sync_dir / 'work-items-detailed.json'
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        total = data.get('total', len(data.get('issues', [])))
        print(f"✅ Fetched {total} issues from Jira")
        print(f"💾 Saved to: {output_file}")
        
        # Show status breakdown
        status_counts = {}
        in_progress = []
        to_do = []
        done = []
        
        for issue in data['issues']:
            status = issue['fields']['status']['name']
            status_counts[status] = status_counts.get(status, 0) + 1
            
            item = {
                'key': issue['key'],
                'summary': issue['fields']['summary']
            }
            
            if status == 'In Progress':
                in_progress.append(item)
            elif status == 'To Do':
                to_do.append(item)
            elif status == 'Done':
                done.append(item)
        
        print('\n📊 Status Breakdown:')
        for status, count in sorted(status_counts.items()):
            emoji = '🟡' if status == 'In Progress' else '⏳' if status == 'To Do' else '✅'
            print(f'  {emoji} {status}: {count}')
        
        if in_progress:
            print('\n🟡 Currently In Progress:')
            for item in in_progress:
                print(f'  - [{item["key"]}] {item["summary"]}')
        else:
            print('\n✅ No tasks currently in progress')
        
        return data
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error fetching from Jira: {e}")
        print(f"Output: {e.stderr}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON response: {e}")
        return None

if __name__ == "__main__":
    fetch_jira_issues()
