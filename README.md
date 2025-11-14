# Daily Git Automation

This script automatically commits and pushes changes to your repository every day.

## Setup

1. **Make the setup script executable and run it:**
   ```bash
   chmod +x setup_automation.sh
   ./setup_automation.sh
   ```

2. **The script will run automatically every day at 9:00 AM**

## Manual Testing

Test the automation script manually:
```bash
python3 automation.py
```

## Configuration

### Change the Schedule

Edit the plist file at `~/Library/LaunchAgents/com.user.gitautomation.plist`

Change the `Hour` and `Minute` values:
```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Hour</key>
    <integer>9</integer>  <!-- Change this -->
    <key>Minute</key>
    <integer>0</integer>  <!-- Change this -->
</dict>
```

After editing, reload the job:
```bash
launchctl unload ~/Library/LaunchAgents/com.user.gitautomation.plist
launchctl load ~/Library/LaunchAgents/com.user.gitautomation.plist
```

## Managing the Automation

**Stop the automation:**
```bash
launchctl unload ~/Library/LaunchAgents/com.user.gitautomation.plist
```

**Start the automation:**
```bash
launchctl load ~/Library/LaunchAgents/com.user.gitautomation.plist
```

**Check if it's running:**
```bash
launchctl list | grep gitautomation
```

## Logs

- Success logs: `automation.log`
- Error logs: `automation.error.log`

## How It Works

The script:
1. Checks for any uncommitted changes in the repository
2. If changes exist, it adds all files (`git add .`)
3. Commits with a timestamp message
4. Pushes to the remote repository
5. Logs all actions with timestamps

## Requirements

- Python 3
- Git configured with push access to your remote repository
- macOS (uses launchd for scheduling)
