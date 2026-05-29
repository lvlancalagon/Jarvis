from jarvis.utils import get_system_stats, get_time_info, get_greeting, check_network, get_project_summary
from jarvis.voice import speak

class JarvisEngine:
    def __init__(self):
        self.persona = "JARVIS"
        self.is_active = True

    def process_command(self, command):
        command = command.lower()

        if "привет" in command or "hello" in command:
            return get_greeting()

        elif "статус" in command or "система" in command:
            stats = get_system_stats()
            net = "Стабильное" if check_network() else "Отсутствует"
            response = (f"Системы функционируют в пределах нормы. Загрузка процессора: {stats['cpu']}%. "
                        f"Память: {stats['memory']}% ({stats['memory_used']}MB/{stats['memory_total']}MB). "
                        f"Диск: {stats['disk']}% ({stats['disk_free']}GB свободно). "
                        f"Сетевое соединение: {net}.")
            return response

        elif "проект" in command or "файлы" in command:
            summary = get_project_summary()
            return f"Анализ структуры проекта завершен, сэр:\n{summary}"

        elif "время" in command or "дата" in command:
            time_str, date_str = get_time_info()
            return f"Текущее время: {time_str}. Дата: {date_str}."

        elif "кто ты" in command:
            return "Я — ДЖАРВИС. Ваш персональный цифровой помощник. К вашим услугам, сэр."

        elif "протокол" in command:
            if "вечеринка" in command or "house party" in command:
                return "Протокол House Party инициирован. Все костюмы приведены в боевую готовность, сэр."
            elif "чистый лист" in command or "clean slate" in command:
                return "Протокол Clean Slate подтвержден. Вы уверены, сэр? Это приведет к самоуничтожению всех систем."
            else:
                return "Доступные протоколы: House Party, Clean Slate. Ожидаю ваших указаний."

        elif "безопасность" in command or "сканируй" in command:
            return "Запускаю глубокое сканирование систем... Угроз не обнаружено. Все брандмауэры активны."

        elif "поиск" in command or "узнай" in command or "найди" in command:
            query = command.replace("поиск", "").replace("узнай", "").replace("найди", "").strip()
            if not query:
                return "Что именно вы хотите найти, сэр?"
            return f"Выполняю поиск по запросу: '{query}'. По моим данным, это требует подключения к глобальной сети. Поиск завершен."

        elif "прощай" in command or "пока" in command or "выход" in command:
            self.is_active = False
            return "Отключаюсь. Всего доброго, сэр."

        else:
            return "Я не совсем вас понял, сэр. Могу я чем-то еще помочь?"

    def handle_interaction(self, user_input, voice_enabled=True):
        response = self.process_command(user_input)
        if voice_enabled:
            # For long responses (like project summary), we might want to speak only a part or a summary
            speech_text = response.split('\n')[0] if '\n' in response else response
            speak(speech_text)
        return response
