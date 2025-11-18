#!/usr/bin/env python3
"""
Test script to demonstrate system metrics tracking.
Run this to see how the metrics module works.
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.system_metrics import SystemMetrics

def demo_json_format():
    """Demo: JSON format (recommended for structured data)"""
    print("=" * 60)
    print("DEMO 1: JSON Format (Recommended)")
    print("=" * 60)
    
    tracker = SystemMetrics("data/demo_metrics.json")
    metrics = tracker.log_metrics(format='json')
    
    print(f"✓ Metrics saved to: data/demo_metrics.json")
    print("\nYou can:")
    print("  - Parse it with Python's json module")
    print("  - Analyze trends over time")
    print("  - Create graphs/charts")
    print("  - Query specific metrics easily")
    

def demo_txt_format():
    """Demo: TXT format (human-readable)"""
    print("\n" + "=" * 60)
    print("DEMO 2: TXT Format (Human-Readable)")
    print("=" * 60)
    
    tracker = SystemMetrics("data/demo_metrics.txt")
    tracker.log_metrics(format='txt')
    
    print(f"✓ Metrics saved to: data/demo_metrics.txt")
    print("\nYou can:")
    print("  - Read it directly in any text editor")
    print("  - Quick visual inspection")
    print("  - Simple but less structured")


def demo_summary():
    """Demo: Get quick summary"""
    print("\n" + "=" * 60)
    print("DEMO 3: Quick Summary")
    print("=" * 60)
    
    tracker = SystemMetrics()
    print(tracker.get_summary())


def demo_individual_metrics():
    """Demo: Access individual metrics programmatically"""
    print("=" * 60)
    print("DEMO 4: Accessing Individual Metrics")
    print("=" * 60)
    
    tracker = SystemMetrics()
    metrics = tracker.collect_metrics()
    
    print("\nYou can access specific values:")
    print(f"  CPU Usage:        {metrics['cpu']['usage_percent']}%")
    print(f"  Memory Used:      {metrics['memory']['used_gb']} GB")
    print(f"  Memory Available: {metrics['memory']['available_gb']} GB")
    print(f"  Disk Free:        {metrics['disk']['free_gb']} GB")
    print(f"  Network Sent:     {metrics['network']['bytes_sent_mb']} MB")
    print(f"  Network Received: {metrics['network']['bytes_recv_mb']} MB")
    
    # Example: Check if resources are low
    print("\n⚠️  Resource Alerts:")
    if metrics['memory']['percent'] > 80:
        print(f"  WARNING: Memory usage high ({metrics['memory']['percent']}%)")
    else:
        print(f"  ✓ Memory OK ({metrics['memory']['percent']}%)")
    
    if metrics['disk']['percent'] > 90:
        print(f"  WARNING: Disk space low ({metrics['disk']['percent']}%)")
    else:
        print(f"  ✓ Disk space OK ({metrics['disk']['percent']}%)")
    
    if metrics['cpu']['usage_percent'] > 80:
        print(f"  WARNING: CPU usage high ({metrics['cpu']['usage_percent']}%)")
    else:
        print(f"  ✓ CPU OK ({metrics['cpu']['usage_percent']}%)")


if __name__ == "__main__":
    print("\n🔧 System Metrics Tracker - Demo\n")
    
    demo_json_format()
    demo_txt_format()
    demo_summary()
    demo_individual_metrics()
    
    print("\n" + "=" * 60)
    print("✅ Demo Complete!")
    print("=" * 60)
    print("\nNext Steps:")
    print("  1. Check the generated files: data/demo_metrics.json & data/demo_metrics.txt")
    print("  2. Your daily_commit.py now automatically tracks metrics")
    print("  3. Run: python scripts/daily_commit.py (or use the scheduled version)")
    print("\n")
