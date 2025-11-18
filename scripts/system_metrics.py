#!/usr/bin/env python3
"""
System Metrics Tracking Module
Tracks CPU, memory, disk, and network usage statistics.
"""

import psutil
import json
from datetime import datetime
from pathlib import Path


class SystemMetrics:
    """Class to collect and store system metrics."""
    
    def __init__(self, log_file="system_metrics.json"):
        """Initialize the metrics tracker.
        
        Args:
            log_file: Path to the log file (JSON or TXT)
        """
        self.log_file = log_file
        self.log_path = Path(log_file)
    
    def collect_metrics(self):
        """Collect current system metrics.
        
        Returns:
            dict: Dictionary containing all system metrics
        """
        # CPU metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        
        # CPU frequency (may not work on all systems, especially macOS)
        try:
            cpu_freq = psutil.cpu_freq()
            freq_current = round(cpu_freq.current, 2) if cpu_freq else None
        except (FileNotFoundError, AttributeError):
            freq_current = None
        
        # Memory metrics
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        # Disk metrics
        disk = psutil.disk_usage('/')
        disk_io = psutil.disk_io_counters()
        
        # Network metrics
        net_io = psutil.net_io_counters()
        
        metrics = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cpu": {
                "usage_percent": cpu_percent,
                "count": cpu_count,
                "frequency_mhz": freq_current
            },
            "memory": {
                "total_gb": round(memory.total / (1024**3), 2),
                "available_gb": round(memory.available / (1024**3), 2),
                "used_gb": round(memory.used / (1024**3), 2),
                "percent": memory.percent
            },
            "swap": {
                "total_gb": round(swap.total / (1024**3), 2),
                "used_gb": round(swap.used / (1024**3), 2),
                "percent": swap.percent
            },
            "disk": {
                "total_gb": round(disk.total / (1024**3), 2),
                "used_gb": round(disk.used / (1024**3), 2),
                "free_gb": round(disk.free / (1024**3), 2),
                "percent": disk.percent
            },
            "disk_io": {
                "read_mb": round(disk_io.read_bytes / (1024**2), 2),
                "write_mb": round(disk_io.write_bytes / (1024**2), 2)
            },
            "network": {
                "bytes_sent_mb": round(net_io.bytes_sent / (1024**2), 2),
                "bytes_recv_mb": round(net_io.bytes_recv / (1024**2), 2),
                "packets_sent": net_io.packets_sent,
                "packets_recv": net_io.packets_recv
            }
        }
        
        return metrics
    
    def save_to_json(self, metrics):
        """Save metrics to JSON file (appends to history).
        
        Args:
            metrics: Dictionary of metrics to save
        """
        # Load existing data or create new list
        if self.log_path.exists():
            with open(self.log_path, 'r') as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, list):
                        data = [data]
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        
        # Append new metrics
        data.append(metrics)
        
        # Save back to file
        with open(self.log_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def save_to_txt(self, metrics):
        """Save metrics to TXT file (human-readable format).
        
        Args:
            metrics: Dictionary of metrics to save
        """
        with open(self.log_path, 'a') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"System Metrics - {metrics['timestamp']}\n")
            f.write(f"{'='*60}\n\n")
            
            # CPU
            f.write(f"CPU:\n")
            f.write(f"  Usage: {metrics['cpu']['usage_percent']}%\n")
            f.write(f"  Cores: {metrics['cpu']['count']}\n")
            if metrics['cpu']['frequency_mhz']:
                f.write(f"  Frequency: {metrics['cpu']['frequency_mhz']} MHz\n")
            
            # Memory
            f.write(f"\nMemory:\n")
            f.write(f"  Total: {metrics['memory']['total_gb']} GB\n")
            f.write(f"  Used: {metrics['memory']['used_gb']} GB ({metrics['memory']['percent']}%)\n")
            f.write(f"  Available: {metrics['memory']['available_gb']} GB\n")
            
            # Disk
            f.write(f"\nDisk (/):\n")
            f.write(f"  Total: {metrics['disk']['total_gb']} GB\n")
            f.write(f"  Used: {metrics['disk']['used_gb']} GB ({metrics['disk']['percent']}%)\n")
            f.write(f"  Free: {metrics['disk']['free_gb']} GB\n")
            
            # Network
            f.write(f"\nNetwork:\n")
            f.write(f"  Sent: {metrics['network']['bytes_sent_mb']} MB\n")
            f.write(f"  Received: {metrics['network']['bytes_recv_mb']} MB\n")
            f.write(f"  Packets Sent: {metrics['network']['packets_sent']}\n")
            f.write(f"  Packets Received: {metrics['network']['packets_recv']}\n")
    
    def log_metrics(self, format='json'):
        """Collect and log system metrics.
        
        Args:
            format: 'json' or 'txt' (default: 'json')
        """
        metrics = self.collect_metrics()
        
        if format == 'json':
            self.save_to_json(metrics)
        else:
            self.save_to_txt(metrics)
        
        return metrics
    
    def get_summary(self):
        """Get a quick summary of current system status.
        
        Returns:
            str: Formatted summary string
        """
        metrics = self.collect_metrics()
        
        summary = f"""
System Status Summary ({metrics['timestamp']})
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CPU:     {metrics['cpu']['usage_percent']}%
Memory:  {metrics['memory']['used_gb']}/{metrics['memory']['total_gb']} GB ({metrics['memory']['percent']}%)
Disk:    {metrics['disk']['used_gb']}/{metrics['disk']['total_gb']} GB ({metrics['disk']['percent']}%)
Network: ↑ {metrics['network']['bytes_sent_mb']} MB | ↓ {metrics['network']['bytes_recv_mb']} MB
"""
        return summary


# Standalone usage example
if __name__ == "__main__":
    print("System Metrics Tracker\n")
    
    # Example 1: JSON format (recommended)
    print("1. Logging to JSON...")
    tracker_json = SystemMetrics("system_metrics.json")
    metrics = tracker_json.log_metrics(format='json')
    print(f"✓ Logged to {tracker_json.log_file}")
    
    # Example 2: TXT format
    print("\n2. Logging to TXT...")
    tracker_txt = SystemMetrics("system_metrics.txt")
    tracker_txt.log_metrics(format='txt')
    print(f"✓ Logged to {tracker_txt.log_file}")
    
    # Example 3: Print summary
    print("\n3. Current System Summary:")
    print(tracker_json.get_summary())
    
    # Example 4: Access individual metrics
    print("\n4. Individual Metrics:")
    print(f"   CPU Usage: {metrics['cpu']['usage_percent']}%")
    print(f"   Memory Available: {metrics['memory']['available_gb']} GB")
    print(f"   Disk Free: {metrics['disk']['free_gb']} GB")
