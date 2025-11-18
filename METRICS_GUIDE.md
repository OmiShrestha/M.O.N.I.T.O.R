# System Metrics Tracking Guide

## 📊 Overview

The `system_metrics.py` module provides comprehensive system monitoring capabilities for tracking:
- **CPU**: Usage percentage, core count, frequency
- **Memory**: Total, used, available, swap
- **Disk**: Total space, used space, free space, I/O operations
- **Network**: Bytes sent/received, packets sent/received

## 🎯 Why JSON over TXT?

### ✅ Use JSON Format When:
- You want structured, queryable data
- Planning to analyze trends over time
- Need to build dashboards or graphs
- Want to parse metrics programmatically
- Need to export to other tools

### 📝 Use TXT Format When:
- You just want quick human readability
- Doing simple manual inspection
- Don't need programmatic access
- Prefer simplicity over structure

**Recommendation: Use JSON** (it's already integrated in your `daily_commit.py`)

---

## 🚀 Quick Start

### 1. Basic Usage

```python
from system_metrics import SystemMetrics

# Create tracker (JSON format)
tracker = SystemMetrics("metrics.json")

# Log metrics
metrics = tracker.log_metrics(format='json')

# Get quick summary
print(tracker.get_summary())
```

### 2. Using with Daily Commits

Your `daily_commit.py` is already configured! It automatically:
- Collects metrics every time it runs
- Saves to `system_metrics.json`
- Commits the metrics file to Git
- Displays a summary in the console

### 3. Switching Between Formats

**For JSON (recommended):**
```python
tracker = SystemMetrics("system_metrics.json")
tracker.log_metrics(format='json')
```

**For TXT (human-readable):**
```python
tracker = SystemMetrics("system_metrics.txt")
tracker.log_metrics(format='txt')
```

---

## 📖 Examples

### Example 1: Monitor Resources
```python
from system_metrics import SystemMetrics

tracker = SystemMetrics()
metrics = tracker.collect_metrics()

# Check if resources are low
if metrics['memory']['percent'] > 80:
    print("⚠️  WARNING: High memory usage!")

if metrics['disk']['percent'] > 90:
    print("⚠️  WARNING: Low disk space!")

if metrics['cpu']['usage_percent'] > 80:
    print("⚠️  WARNING: High CPU usage!")
```

### Example 2: Access Individual Metrics
```python
from system_metrics import SystemMetrics

tracker = SystemMetrics()
metrics = tracker.collect_metrics()

print(f"CPU: {metrics['cpu']['usage_percent']}%")
print(f"Memory: {metrics['memory']['used_gb']} GB used")
print(f"Disk: {metrics['disk']['free_gb']} GB free")
print(f"Network Sent: {metrics['network']['bytes_sent_mb']} MB")
```

### Example 3: Analyze Historical Data (JSON)
```python
import json

# Read all historical metrics
with open('system_metrics.json', 'r') as f:
    history = json.load(f)

# Find average CPU usage
cpu_values = [entry['cpu']['usage_percent'] for entry in history]
avg_cpu = sum(cpu_values) / len(cpu_values)
print(f"Average CPU usage: {avg_cpu:.2f}%")

# Find peak memory usage
max_memory = max(entry['memory']['percent'] for entry in history)
print(f"Peak memory usage: {max_memory}%")
```

---

## 🔧 Integration in Your Project

### Current Setup
Your project is already configured! Here's what happens:

1. **daily_commit.py** runs (3 times daily: 3 PM, 6 PM, 9 PM)
2. System metrics are collected automatically
3. Metrics saved to `system_metrics.json`
4. Both `daily_log.txt` and `system_metrics.json` are committed to Git
5. Summary printed to console

### To Change Format to TXT

In `daily_commit.py`, change line 28:
```python
# From:
metrics = metrics_tracker.log_metrics(format='json')

# To:
metrics = metrics_tracker.log_metrics(format='txt')
```

And update the METRICS_FILE constant:
```python
METRICS_FILE = "system_metrics.txt"  # instead of .json
```

---

## 📁 File Structure

```
automation/
├── daily_commit.py          # Main script (metrics integrated)
├── system_metrics.py        # Metrics module (NEW)
├── test_metrics.py          # Demo/test script (NEW)
├── requirements.txt         # Updated with psutil
├── system_metrics.json      # Metrics log (generated)
└── daily_log.txt           # Commit log
```

---

## 🧪 Testing

Run the test script to see all features:
```bash
source .venv/bin/activate
python test_metrics.py
```

This will:
- Generate `demo_metrics.json` (structured data)
- Generate `demo_metrics.txt` (human-readable)
- Show current system summary
- Demonstrate accessing individual metrics
- Show resource alerts

---

## 💡 Advanced Use Cases

### 1. Custom Alerts
```python
from system_metrics import SystemMetrics

tracker = SystemMetrics()
metrics = tracker.collect_metrics()

# Email/notify when disk space is low
if metrics['disk']['free_gb'] < 10:
    send_alert("Disk space critically low!")
```

### 2. Performance Monitoring
```python
import json
from datetime import datetime

with open('system_metrics.json', 'r') as f:
    history = json.load(f)

# Get last 24 hours of data
recent = [m for m in history if is_within_24h(m['timestamp'])]

# Calculate averages
avg_cpu = sum(m['cpu']['usage_percent'] for m in recent) / len(recent)
avg_mem = sum(m['memory']['percent'] for m in recent) / len(recent)
```

### 3. Export to CSV
```python
import json
import csv

with open('system_metrics.json', 'r') as f:
    data = json.load(f)

with open('metrics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'CPU %', 'Memory %', 'Disk %'])
    
    for entry in data:
        writer.writerow([
            entry['timestamp'],
            entry['cpu']['usage_percent'],
            entry['memory']['percent'],
            entry['disk']['percent']
        ])
```

---

## 🎓 Key Takeaways

1. **Modularity**: `system_metrics.py` is separate - you can use it in any project
2. **Flexibility**: Switch between JSON/TXT formats easily
3. **Integration**: Already works with your daily commits
4. **Scalability**: JSON format allows for future analytics and visualization
5. **Cross-platform**: Works on macOS, Linux, and Windows

---

## 📊 Metrics Reference

### CPU Metrics
- `usage_percent`: Current CPU usage (%)
- `count`: Number of CPU cores
- `frequency_mhz`: CPU frequency (may be null on some systems)

### Memory Metrics
- `total_gb`: Total RAM
- `used_gb`: Used RAM
- `available_gb`: Available RAM
- `percent`: Memory usage percentage

### Disk Metrics
- `total_gb`: Total disk space
- `used_gb`: Used disk space
- `free_gb`: Free disk space
- `percent`: Disk usage percentage
- `read_mb`: Total MB read from disk
- `write_mb`: Total MB written to disk

### Network Metrics
- `bytes_sent_mb`: Total MB sent
- `bytes_recv_mb`: Total MB received
- `packets_sent`: Total packets sent
- `packets_recv`: Total packets received

---

## 🆘 Troubleshooting

**Q: Import error for psutil?**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Q: Want to change logging frequency?**
Edit the schedule in `daily_commit.py`:
```python
schedule.every().hour.do(make_daily_commit)  # Every hour
schedule.every(30).minutes.do(make_daily_commit)  # Every 30 min
```

**Q: Want to track specific disk partitions?**
Modify `system_metrics.py` line 43:
```python
disk = psutil.disk_usage('/path/to/partition')
```

**Q: Need to clear history?**
```bash
# JSON format - creates new array
echo "[]" > system_metrics.json

# TXT format - clear file
> system_metrics.txt
```

---

## 📚 Resources

- [psutil Documentation](https://psutil.readthedocs.io/)
- [Python JSON Module](https://docs.python.org/3/library/json.html)
- [System Monitoring Best Practices](https://en.wikipedia.org/wiki/System_monitor)

---

**Happy Monitoring! 📊**
