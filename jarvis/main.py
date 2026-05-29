import sys
import os

# Add parent directory to sys.path to allow imports from 'jarvis'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jarvis.engine import JarvisEngine

def main():
    engine = JarvisEngine()
    print("--- JARVIS: Система инициализирована ---")
    print("Тип: 'выход' для завершения.")

    while engine.is_active:
        try:
            user_input = input("Вы: ")
            if not user_input.strip():
                continue

            response = engine.handle_interaction(user_input)
            print(f"JARVIS: {response}")
            print("(Голосовой ответ сохранен в response.mp3)")

        except KeyboardInterrupt:
            print("\nJARVIS: Экстренное завершение работы.")
            break
        except Exception as e:
            print(f"JARVIS: Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
