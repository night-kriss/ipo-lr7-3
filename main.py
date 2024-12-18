import json
import os

# Инициализация данных
filename = 'cities.json'
if not os.path.exists(filename):
    data = [
        {"id": 1, "name": "Минск", "country": "Беларусь", "is_big": True, "people_count": 2000000},
        {"id": 2, "name": "Москва", "country": "Россия", "is_big": True, "people_count": 12500000},
        {"id": 3, "name": "Киев", "country": "Украина", "is_big": True, "people_count": 2800000},
        {"id": 4, "name": "Вильнюс", "country": "Литва", "is_big": False, "people_count": 500000},
        {"id": 5, "name": "Рига", "country": "Латвия", "is_big": False, "people_count": 700000}
    ]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Основная программа
operations_count = 0

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for record in data:
                print(f"ID: {record['id']}, Название: {record['name']}, Страна: {record['country']}, "
                      f"Большой город: {record['is_big']}, Население: {record['people_count']}")
        operations_count += 1

    elif choice == '2':
        search_id = int(input("Введите ID записи: "))
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for index, record in enumerate(data):
                if record['id'] == search_id:
                    print(f"=============== Найдено ===============")
                    print(f"Позиция: {index}, ID: {record['id']}, Название: {record['name']}, Страна: {record['country']}, "
                          f"Большой город: {record['is_big']}, Население: {record['people_count']}")
                    found = True
                    break
            if not found:
                print("=============== Не найдено ===============")
        operations_count += 1

    elif choice == '3':
        new_id = int(input("Введите ID: "))
        new_name = input("Введите название города: ")
        new_country = input("Введите название страны: ")
        new_is_big = input("Является ли город большим (True/False): ").lower() == 'true'
        new_people_count = int(input("Введите население города: "))
        new_record = {
            "id": new_id,
            "name": new_name,
            "country": new_country,
            "is_big": new_is_big,
            "people_count": new_people_count
        }
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data.append(new_record)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Запись добавлена.")
        operations_count += 1

    elif choice == '4':
        delete_id = int(input("Введите ID записи для удаления: "))
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        new_data = [record for record in data if record['id'] != delete_id]
        if len(new_data) == len(data):
            print("=============== Не найдено ===============")
        else:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(new_data, file, ensure_ascii=False, indent=4)
            print("Запись удалена.")
        operations_count += 1

    elif choice == '5':
        print(f"Количество выполненных операций: {operations_count}")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
