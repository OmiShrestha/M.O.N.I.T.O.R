#!/usr/bin/env python3
"""
Daily Git Automation Script
Automatically commits and pushes changes to the repository.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_command(command, cwd=None):
    """Execute a shell command and return the result."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        return None


def check_git_status(repo_path):
    """Check if there are any changes to commit."""
    status = run_command("git status --porcelain", cwd=repo_path)
    return status is not None and len(status) > 0


def create_activity_log(repo_path):
    """Create or update an activity log file to ensure there's always a change."""
    log_file = Path(repo_path) / ".activity_log.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append timestamp to activity log
    with open(log_file, 'a') as f:
        f.write(f"Automated run: {timestamp}\n")
    
    print(f"[{timestamp}] Activity logged.")


def git_commit_and_push(repo_path):
    """Commit and push changes to the repository."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Always create an activity log entry to ensure there's a change
    create_activity_log(repo_path)
    
    # Add all changes
    print(f"[{timestamp}] Adding changes...")
    if run_command("git add .", cwd=repo_path) is None:
        return False
    
    # Commit with timestamp
    commit_message = f"Auto-commit: {timestamp}"
    print(f"[{timestamp}] Committing changes...")
    if run_command(f'git commit -m "{commit_message}"', cwd=repo_path) is None:
        return False
    
    # Push to remote
    print(f"[{timestamp}] Pushing to remote...")
    if run_command("git push", cwd=repo_path) is None:
        return False
    
    print(f"[{timestamp}] Successfully committed and pushed changes!")
    return True


def main():
    """Main function to run the automation."""
    # Get the repository path (parent directory of this script)
    repo_path = Path(__file__).parent.absolute()
    
    print(f"Running automation for repository: {repo_path}")
    
    # Perform git commit and push
    success = git_commit_and_push(repo_path)
    
    if not success:
        print("Automation failed!")
        sys.exit(1)
    
    print("Automation completed successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()
