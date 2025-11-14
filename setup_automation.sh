#!/bin/bash
# Setup script for daily automation using launchd (macOS)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST_FILE="$HOME/Library/LaunchAgents/com.user.gitautomation.plist"

# Make the Python script executable
chmod +x "$SCRIPT_DIR/automation.py"

# Create the launchd plist file
cat > "$PLIST_FILE" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.gitautomation</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$SCRIPT_DIR/automation.py</string>
    </array>
    
    <key>WorkingDirectory</key>
    <string>$SCRIPT_DIR</string>
    
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    
    <key>StandardOutPath</key>
    <string>$SCRIPT_DIR/automation.log</string>
    
    <key>StandardErrorPath</key>
    <string>$SCRIPT_DIR/automation.error.log</string>
    
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

# Load the launchd job
launchctl unload "$PLIST_FILE" 2>/dev/null
launchctl load "$PLIST_FILE"

echo "✓ Automation setup complete!"
echo "  - The script will run daily at 9:00 AM"
echo "  - Logs will be saved to: $SCRIPT_DIR/automation.log"
echo "  - Errors will be saved to: $SCRIPT_DIR/automation.error.log"
echo ""
echo "To change the time, edit: $PLIST_FILE"
echo "To unload the automation, run: launchctl unload $PLIST_FILE"
echo "To test now, run: python3 $SCRIPT_DIR/automation.py"
