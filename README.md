# automated system monitoring with daily commit logs

**An intelligent automation that keeps your GitHub active while tracking system health metrics.**

A Python-based automation tool that performs scheduled commits and maintains daily updates while simultaneously monitoring and logging system performance metric such as CPU, memory, disk and network.

---

## Features

- **Automated Daily Commits** - Maintains GitHub contribution graph with 3 commits daily
- **System Metrics Tracking** - Monitors CPU, memory, disk space, and network activity
- **Smart Scheduling** - Runs at 9 AM, 2 PM, and 8 PM automatically
- **Professional Commit Messages** - Shows actual system metrics in commit history
- **Privacy-Focused** - Metrics stored locally, only commit logs pushed to GitHub
- **Modular Design** - Clean separation between scripts and data

---

## What It Does

Every day at **9:00 AM, 2:00 PM, and 8:00 PM**, the automation:

1. Collects current system metrics (CPU, memory, disk, network)
2. Logs metrics locally in `data/system_metrics.json`
3. Updates `data/daily_log.txt` with formatted entry
4. Creates professional Git commit with metrics in message
5. Pushes to GitHub automatically

**Example commit messages:**
```
Morning health check: CPU 23% | Memory 73% | Disk 21.6% used
Afternoon monitoring: CPU 45% | Memory 78% | Disk 21.7% used
Evening baseline: CPU 18% | Memory 65% | Disk 22% used
```

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Automation

```bash
nohup .venv/bin/python3 scripts/daily_commit.py > automation.log 2>&1 &
```

### 3. Verify It's Running

```bash
pgrep -f daily_commit.py
```

That's it! Your automation is now running in the background.

---

## Project Structure

```
automation/
├── scripts/              # Python modules
│   ├── daily_commit.py   # Main automation script
│   ├── system_metrics.py # Metrics collection module
│   └── test_metrics.py   # Demo/testing script
│
├── data/                 # Data files
│   ├── daily_log.txt     # Commit history (pushed to Git)
│   └── system_metrics.json # Metrics data (local only)
│
├── COMMANDS.txt          # Quick command reference
├── METRICS_GUIDE.md      # Detailed metrics documentation
└── requirements.txt      # Python dependencies
```

---

## Management Commands

See `COMMANDS.txt` for full reference, or use these:

```bash
# Check status
pgrep -f daily_commit.py

# Stop automation
pkill -f daily_commit.py

# View logs
tail -f automation.log

# Test metrics collection
python scripts/test_metrics.py
```

---

## System Metrics

The automation tracks:

- **CPU**: Usage percentage, core count, frequency
- **Memory**: Total, used, available RAM + swap
- **Disk**: Total, used, free space + I/O statistics
- **Network**: Bytes sent/received, packet counts

All metrics are saved locally in JSON format for easy analysis and historical tracking.

---

## Configuration

### Change Schedule Times

Edit `scripts/daily_commit.py`:

```python
schedule.every().day.at("09:00").do(make_daily_commit)  # 9 AM
schedule.every().day.at("14:00").do(make_daily_commit)  # 2 PM
schedule.every().day.at("20:00").do(make_daily_commit)  # 8 PM
```

### Change Metrics Format

In `scripts/daily_commit.py`, change:

```python
metrics_tracker.log_metrics(format='json')  # or 'txt' for text format
```

---

## Use Cases

- Maintain active GitHub profile for recruiters
- Track system performance over time
- Monitor resource usage patterns
- Demonstrate automation skills
- Learn Python scheduling and system monitoring

---

## Documentation

- **`COMMANDS.txt`** - Essential commands for managing automation
- **`METRICS_GUIDE.md`** - Comprehensive guide to metrics tracking
- **`scripts/test_metrics.py`** - Run for interactive demo

---

## Privacy & Security

- System metrics are **NOT pushed to GitHub** (see `.gitignore`)
- Only timestamp logs are committed
- No sensitive system information exposed
- All data stays on your local machine

---

## Contributing

This is a personal automation project, but feel free to fork and customize for your own use!

---

## License

MIT License - Feel free to use and modify as needed.

---

**Made with love for maintaining GitHub streaks and monitoring system health**
