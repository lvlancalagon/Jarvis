import psutil
import datetime
import os
import socket

def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    return {
        "cpu": cpu_usage,
        "memory": memory_info.percent,
        "memory_used": memory_info.used // (1024 * 1024),
        "memory_total": memory_info.total // (1024 * 1024),
        "disk": disk_info.percent,
        "disk_free": disk_info.free // (1024 * 1024 * 1024)
    }

def get_time_info():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S"), now.strftime("%d %B %Y")

def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Доброе утро, сэр."
    elif 12 <= hour < 18:
        return "Добрый день, сэр."
    elif 18 <= hour < 23:
        return "Добрый вечер, сэр."
    else:
        return "Доброй ночи, сэр. Работаете допоздна?"

def check_network():
    try:
        # Check if we can connect to a common DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def get_project_summary(path="."):
    summary = []
    for root, dirs, files in os.walk(path):
        if ".git" in root or "__pycache__" in root:
            continue
        level = root.replace(path, "").count(os.sep)
        indent = " " * 4 * (level)
        summary.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for f in files:
            size = os.path.getsize(os.path.join(root, f)) // 1024
            summary.append(f"{sub_indent}{f} ({size} KB)")
    return "\n".join(summary)

if __name__ == "__main__":
    print(f"Stats: {get_system_stats()}")
    print(f"Time: {get_time_info()}")
    print(f"Greeting: {get_greeting()}")
    print(f"Network: {'Online' if check_network() else 'Offline'}")
    print("Project Summary:")
    print(get_project_summary())
