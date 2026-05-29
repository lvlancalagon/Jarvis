from jarvis.utils import get_system_stats, get_time_info, get_greeting
from jarvis.voice import speak

class JarvisEngine:
    def __init__(self):
        self.persona = "JARVIS"
        self.is_active = True

    def process_command(self, command):
        command = command.lower()

        if "привет" in command or "hello" in command:
            response = get_greeting()
            return response

        elif "статус" in command or "система" in command:
            stats = get_system_stats()
            response = f"Системы функционируют в пределах нормы. Загрузка процессора: {stats['cpu']}%. Память: {stats['memory']}% использовано."
            return response

        elif "время" in command or "дата" in command:
            time_str, date_str = get_time_info()
            response = f"Текущее время: {time_str}. Дата: {date_str}."
            return response

        elif "кто ты" in command:
            response = "Я — ДЖАРВИС. Ваш персональный цифровой помощник. К вашим услугам, сэр."
            return response

        elif "прощай" in command or "пока" in command or "выход" in command:
            self.is_active = False
            return "Отключаюсь. Всего доброго, сэр."

        else:
            return "Я не совсем вас понял, сэр. Могу я чем-то еще помочь?"

    def handle_interaction(self, user_input, voice_enabled=True):
        response = self.process_command(user_input)
        if voice_enabled:
            speak(response)
        return response
