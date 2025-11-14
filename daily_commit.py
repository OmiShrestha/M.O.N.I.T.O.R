#!/usr/bin/env python3
"""
Automated Daily Git Commit Script
This script creates a daily commit with current date and time.
"""

import os
import subprocess
from datetime import datetime
import time
import schedule

# Configuration
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = "daily_log.txt"


def make_daily_commit():
    """Create a commit  with current date and time."""
    try:
        os.chdir(REPO_PATH)
        
        # Get current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        date_str = now.strftime("%Y-%m-%d")
        
        # Create or update log file
        log_path = os.path.join(REPO_PATH, LOG_FILE)
        with open(log_path, 'a') as f:
            f.write(f"Automated commit: {timestamp}\n")
        
        # Git operations
        subprocess.run(['git', 'add', LOG_FILE], check=True)
        
        commit_message = f"Automated daily commit - {timestamp}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # Push to remote
        subprocess.run(['git', 'push'], check=True)
        
        print(f"✓ Successfully committed and pushed at {timestamp}")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Git error: {e}")
    except Exception as e:
        print(f"✗ Error: {e}")


def run_scheduler():
    """Run the scheduler that executes daily commits."""
    # Schedule the task to run three times daily: 3 PM, 6 PM, and 9 PM
    schedule.every().day.at("15:00").do(make_daily_commit)  # 3:00 PM
    schedule.every().day.at("18:00").do(make_daily_commit)  # 6:00 PM
    schedule.every().day.at("21:00").do(make_daily_commit)  # 9:00 PM
    
    print("Daily commit automation started!")
    print("Scheduled to run at: 3:00 PM, 6:00 PM, and 9:00 PM")
    print("Press Ctrl+C to stop\n")
    
    # Run immediately on start
    print("Running initial commit now...")
    make_daily_commit()
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        print("\n\nAutomation stopped by user.")
