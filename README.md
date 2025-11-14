# Daily Git Automation

This project automatically creates and pushes a git commit every day with the current date and time.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure your git repository is configured with a remote:
   ```bash
   git remote -v
   ```

3. Ensure you have git credentials configured (so you don't need to enter password each time)

## Running Options

### Option 1: Run as a Long-Running Process

Run the script directly - it will keep running and make daily commits:

```bash
python3 daily_commit.py
```

This will commit and push every day at 9:00 AM. To change the time, edit the schedule in the script.

### Option 2: Use macOS LaunchAgent (Recommended for macOS)

Create a file `~/Library/LaunchAgents/com.daily.commit.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.daily.commit</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/theomigod/Downloads/automation/daily_commit.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/daily_commit.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/daily_commit.error.log</string>
</dict>
</plist>
```

Load it with:
```bash
launchctl load ~/Library/LaunchAgents/com.daily.commit.plist
```

### Option 3: Use Cron

Add to crontab (`crontab -e`):
```
0 9 * * * cd /Users/theomigod/Downloads/automation && /usr/bin/python3 daily_commit.py
```

## What It Does

- Creates/updates `daily_log.txt` with timestamp
- Commits the change with a timestamped message
- Pushes to the remote repository
- Runs automatically every day

## Customization

- Change the schedule time in `daily_commit.py` (line with `schedule.every().day.at("09:00")`)
- Modify what gets committed by editing the `make_daily_commit()` function
