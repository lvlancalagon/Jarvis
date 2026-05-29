import psutil
import datetime
import os

def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    return {
        "cpu": cpu_usage,
        "memory": memory_info.percent,
        "memory_used": memory_info.used // (1024 * 1024),
        "memory_total": memory_info.total // (1024 * 1024)
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

if __name__ == "__main__":
    print(f"Stats: {get_system_stats()}")
    print(f"Time: {get_time_info()}")
    print(f"Greeting: {get_greeting()}")
