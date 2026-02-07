import os
from datetime import datetime

MEMORY_DIR = "memory"
MEMORY_FILE = os.path.join(MEMORY_DIR, "history.txt")


def ensure_memory():
    os.makedirs(MEMORY_DIR, exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            f.write("=== AI Agent Memory ===\n")


def read_memory(limit=4000):
    try:
        with open(MEMORY_FILE, "r") as f:
            data = f.read()
            return data[-limit:]
    except:
        return ""


def append_memory(entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MEMORY_FILE, "a") as f:
        f.write(f"\n[{timestamp}] {entry}\n")