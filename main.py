import csv
import json

# Функція для створення .csv файлу
def create_csv(file_path):
    # Створюємо список даних, які записуватимуться у файл
    data = [
        ["name", "age", "grade"],
        ["Тихонов Богдан", 19, 95],
        ["Лободюк Євгеній", 19, 100],
        ["Ткаченко Ілля", 19, 95],
        ["Срібна Ольга", 20, 70],
        ["Росієнко Олексій", 19, 82],
    ]

    try:
        # Відкриваємо CSV файл для запису
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Записуємо рядки даних у файл
            writer.writerows(data)
        print(f"CSV файл '{file_path}' створено успішно.")
    except Exception as e:
        # Обробляємо будь-які помилки при створенні файлу
        print(f"Помилка під час створення CSV файлу: {e}")


# Функція для конвертації даних із .csv у .json
def csv_to_json(csv_file, json_file):
    try:
        # Відкриваємо CSV файл для читання
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Читаємо CSV у вигляді словників
            data = [row for row in reader]  # Створюємо список словників із рядків файлу

        # Відкриваємо JSON файл для запису даних
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Записуємо дані у JSON форматі
        print(f"Дані успішно сконвертовані з '{csv_file}' у '{json_file}'.")
    except FileNotFoundError:
        # Обробляємо помилку, якщо CSV файл не знайдено
        print(f"Файл '{csv_file}' не знайдено!")
    except Exception as e:
        # Обробляємо інші можливі помилки
        print(f"Помилка під час конвертації: {e}")


# Основна функція програми
def main():
    csv_file = 'students.csv'  # Назва CSV файлу
    json_file = 'students.json'  # Назва JSON файлу

    # Створюємо CSV файл із даними студентів
    create_csv(csv_file)

    # Конвертуємо дані з CSV у JSON
    csv_to_json(csv_file, json_file)


# Запуск основної програми
if __name__ == "__main__":
    main()
