import json
import matplotlib.pyplot as plt

DATA_FILE = "students.json"
RESULT_FILE = "birthdays.json"

def plot_gender_pie_chart():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            students = json.load(f)

        male_count = sum(1 for s in students if s["gender"].lower() == 'ч')
        female_count = sum(1 for s in students if s["gender"].lower() == 'ж')

        labels = ['Хлопці', 'Дівчата']
        sizes = [male_count, female_count]
        colors = ['skyblue', 'lightcoral']
        explode = (0.05, 0.05)  

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, shadow=True, startangle=140)
        plt.title('Співвідношення хлопців і дівчат у класі')
        plt.axis('equal')  

        plt.show()

    except FileNotFoundError:
        print("Файл з даними не знайдено.")
    except json.JSONDecodeError:
        print("Помилка у форматі JSON.")

plot_gender_pie_chart()

def create_sample_data():
    students = [
        {"last_name": "Іваненко", "first_name": "Олена", "middle_name": "Петрівна", "birth_date": [2008, 3, 21], "gender": "ж"},
        {"last_name": "Коваленко", "first_name": "Олег", "middle_name": "Ігорович", "birth_date": [2007, 7, 5], "gender": "ч"},
        {"last_name": "Сидоренко", "first_name": "Марія", "middle_name": "Олександрівна", "birth_date": [2008, 3, 17], "gender": "ж"},
        {"last_name": "Шевченко", "first_name": "Андрій", "middle_name": "Вікторович", "birth_date": [2007, 11, 30], "gender": "ч"},
        {"last_name": "Мельник", "first_name": "Катерина", "middle_name": "Богданівна", "birth_date": [2007, 5, 22], "gender": "ж"},
        {"last_name": "Петренко", "first_name": "Ігор", "middle_name": "Сергійович", "birth_date": [2008, 3, 10], "gender": "ч"},
        {"last_name": "Ткаченко", "first_name": "Наталія", "middle_name": "Григорівна", "birth_date": [2008, 8, 15], "gender": "ж"},
        {"last_name": "Бондар", "first_name": "Євген", "middle_name": "Дмитрович", "birth_date": [2007, 1, 9], "gender": "ч"},
        {"last_name": "Лисенко", "first_name": "Світлана", "middle_name": "Іванівна", "birth_date": [2008, 3, 5], "gender": "ж"},
        {"last_name": "Гаврилюк", "first_name": "Олексій", "middle_name": "Михайлович", "birth_date": [2007, 9, 2], "gender": "ч"}
    ]
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

# Виведення вмісту JSON файлу
def display_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            students = json.load(f)
            for student in students:
                print(student)
    except FileNotFoundError:
        print("Файл не знайдено. Створіть файл спочатку.")

# Додавання нового запису
def add_student():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []

    print("Введіть дані учня:")
    student = {
        "last_name": input("Прізвище: "),
        "first_name": input("Ім'я: "),
        "middle_name": input("По батькові: "),
        "birth_date": [
            int(input("Рік народження: ")),
            int(input("Місяць народження (1-12): ")),
            int(input("День народження: "))
        ],
        "gender": input("Стать (ч/ж): ")
    }
    students.append(student)

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
    print("Успішно додано.")

# Видалення запису за прізвищем
def delete_student():
    name_to_delete = input("Введіть прізвище учня для видалення: ")
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            students = json.load(f)
        new_students = [s for s in students if s["last_name"].lower() != name_to_delete.lower()]
        if len(new_students) < len(students):
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(new_students, f, ensure_ascii=False, indent=4)
            print("Запис видалено.")
        else:
            print("Запис не знайдено.")
    except FileNotFoundError:
        print("Файл не знайдено.")

# Пошук за будь-яким полем
def search_student():
    field = input("Введіть поле для пошуку (last_name, gender, etc): ")
    value = input("Введіть значення для пошуку: ")
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            students = json.load(f)
            results = [s for s in students if str(s.get(field, '')).lower() == value.lower()]
            if results:
                for r in results:
                    print(r)
            else:
                print("Нічого не знайдено.")
    except FileNotFoundError:
        print("Файл не знайдено.")

# Завдання: знайти учнів, народжених у певному місяці
def find_birthdays_by_month():
    try:
        month = int(input("Введіть номер місяця (1-12): "))
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            students = json.load(f)
        found = [s for s in students if s['birth_date'][1] == month]

        if found:
            print("Учні, народжені у цьому місяці:")
            for s in found:
                print(f"{s['first_name']} {s['last_name']}")
        else:
            print("Немає учнів з днем народження у цьому місяці.")

        # Зберігаємо результат у інший JSON файл
        with open(RESULT_FILE, 'w', encoding='utf-8') as f:
            json.dump(found if found else [{"message": "Немає учнів у цьому місяці"}], f, ensure_ascii=False, indent=4)
        print(f"Результат записано у файл {RESULT_FILE}")

    except ValueError:
        print("Введено некоректний місяць.")

def main():
    while True:
        print("\nОберіть опцію:")
        print("1. Створити початкові дані")
        print("2. Вивести дані")
        print("3. Додати учня")
        print("4. Видалити учня")
        print("5. Пошук за полем")
        print("6. Учні, народжені у заданому місяці")
        print("7. Побудувати кругову діаграму за статтю")

        print("0. Вихід")

        choice = input("Ваш вибір: ")
        if choice == '1':
            create_sample_data()
        elif choice == '2':
            display_data()
        elif choice == '3':
            add_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            find_birthdays_by_month()
        elif choice == '7':
            plot_gender_pie_chart()

        elif choice == '0':
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
main()
