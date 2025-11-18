# automated system monitoring w/ daily commit logs

**intelligent automation that keeps your github active while tracking system health metrics.**

python-based automation tool that performs scheduled commits and maintains daily updates while simultaneously monitoring and logging system performance metrics such as cpu, memory, disk and network.

---

## features

- **system metrics tracking** - monitors cpu, memory, disk space, and network activity
- **smart scheduling** - runs at 9 am, 2 pm, and 8 pm automatically
- **professional commit messages** - shows actual system metrics in commit history
- **privacy-focused** - metrics stored locally, only commit logs pushed to github
- **modular design** - clean separation between scripts and data

---

## what it does

every day at **9:00 am, 2:00 pm, and 8:00 pm**, the automation:

1. collects current system metrics (cpu, memory, disk, network)
2. logs metrics locally in `data/system_metrics.json`
3. updates `data/daily_log.txt` with formatted entry
4. creates professional git commit with metrics in message
5. pushes to github automatically

**example commit messages:**
```
Morning health check: CPU 23% | Memory 73% | Disk 21.6% used
Afternoon monitoring: CPU 45% | Memory 78% | Disk 21.7% used
Evening baseline: CPU 18% | Memory 65% | Disk 22% used
```

---

## quick start

### 1. install dependencies

```bash
pip install -r requirements.txt
```

### 2. start automation

```bash
nohup .venv/bin/python3 scripts/daily_commit.py > automation.log 2>&1 &
```

### 3. verify it's running

```bash
pgrep -f daily_commit.py
```

that's it. your automation is now running in the background.

---

## project structure

```
automation/
├── scripts/              # python modules
│   ├── daily_commit.py   # main automation script
│   ├── system_metrics.py # metrics collection module
│   └── test_metrics.py   # demo/testing script
│
├── data/                 # data files
│   ├── daily_log.txt     # commit history (pushed to git)
│   └── system_metrics.json # metrics data (local only)
│
├── COMMANDS.txt          # quick command reference
├── METRICS_GUIDE.md      # detailed metrics documentation
└── requirements.txt      # python dependencies
```

---

## management commands

see `COMMANDS.txt` for full reference, or use these:

```bash
# check status
pgrep -f daily_commit.py

# stop automation
pkill -f daily_commit.py

# view logs
tail -f automation.log

# test metrics collection
python scripts/test_metrics.py
```

---

## system metrics

the automation tracks:

- **cpu**: usage percentage, core count, frequency
- **memory**: total, used, available ram + swap
- **disk**: total, used, free space + i/o statistics
- **network**: bytes sent/received, packet counts

all metrics are saved locally in json format for easy analysis and historical tracking.

---

## configuration

### change schedule times

edit `scripts/daily_commit.py`:

```python
schedule.every().day.at("09:00").do(make_daily_commit)  # 9 am
schedule.every().day.at("14:00").do(make_daily_commit)  # 2 pm
schedule.every().day.at("20:00").do(make_daily_commit)  # 8 pm
```

### change metrics format

in `scripts/daily_commit.py`, change:

```python
metrics_tracker.log_metrics(format='json')  # or 'txt' for text format
```

---

## use cases

- track system performance over time
- monitor resource usage patterns
- demonstrate automation skills
- learn python scheduling and system monitoring

---

## documentation

- **`COMMANDS.txt`** - essential commands for managing automation
- **`METRICS_GUIDE.md`** - comprehensive guide to metrics tracking
- **`scripts/test_metrics.py`** - run for interactive demo

---

## privacy & security

- system metrics are **not pushed to github** (see `.gitignore`)
- only timestamp logs are committed
- no sensitive system information exposed
- all data stays on your local machine

---

## contributing

this is a personal automation project, but feel free to fork and customize for your own personal use.

---

## license

mit license - feel free to use and modify as needed.

---
