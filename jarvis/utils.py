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
        return "Доброе утро, сэр. Готовы к тестированию или новому контенту?"
    elif 12 <= hour < 18:
        return "Добрый день, сэр. Каналы растут, системы стабильны."
    elif 18 <= hour < 23:
        return "Добрый вечер, сэр. Время для монтажа или проверки багов?"
    else:
        return "Доброй ночи, сэр. Ночной рендеринг или поиск критических багов?"

def check_network():
    try:
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

def get_testing_checklists():
    return {
        "UI/UX": [
            "Проверить адаптивность под разные разрешения",
            "Проверить отображение шрифтов и иконок",
            "Проверить кликабельность всех кнопок и ссылок",
            "Проверить контрастность и читаемость текста"
        ],
        "Functional": [
            "Проверить формы регистрации и логина",
            "Проверить поиск по сайту",
            "Проверить работу корзины и оплаты",
            "Проверить валидацию полей ввода"
        ],
        "Cross-Browser": [
            "Проверить в Chrome, Firefox, Safari, Edge",
            "Проверить мобильные версии (iOS, Android)"
        ]
    }

def get_youtube_ideas():
    return {
        "Garry's Mod": {
            "Ideas": [
                "Топ 10 хоррор карт в GMod",
                "Эксперименты с физикой: 1000 NPC vs 1 игрок",
                "Строительство секретной базы в GMod"
            ],
            "Tags": "gmod, garrys mod, sandbox, гмод, песочница"
        },
        "Sprunki": {
            "Ideas": [
                "Sprunki: Все секретные комбинации звуков",
                "Sprunki Incredibox: Создание идеального микса",
                "Sprunki: Эволюция персонажей"
            ],
            "Tags": "sprunki, incredibox, music, game, спрунки"
        },
        "Italian Brainrot": {
            "Ideas": [
                "Italian Brainrot Compilation #1",
                "Why Italian Brainrot is taking over YouTube",
                "Memes you only understand in Italy (Brainrot Edition)"
            ],
            "Tags": "italian brainrot, memes, brainrot, tiktok, youtube shorts"
        }
    }

def get_channel_management_tips():
    return [
        "Используйте разные профили браузера для каждого канала",
        "Планируйте публикации заранее через творческую студию",
        "Оптимизируйте метаданные (теги, описание) для каждого видео",
        "Следите за аналитикой удержания аудитории"
    ]
