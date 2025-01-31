from datetime import datetime

def get_days_from_today(date):
    """
    Обчислює кількість днів між заданою датою і поточною датою.

    Параметри:
    - date (str): Дата у форматі 'РРРР-ММ-ДД'.

    Повертає:
    - int: Кількість днів між сьогоднішньою датою і заданою.
           Від'ємне число, якщо задана дата в майбутньому.
    """
    while True:
        # Перетворення рядка дати у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        try:
            # Поточна дата
            today = datetime.today().date()
            # Різниця між датами
            delta = today - given_date
            return delta.days
            break
        except ValueError:
            # Обробка винятків для неправильного формату дати
            print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД' ")
        finally:
            print('.' * 60)


# Приклад використання
given_date = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09') ")
result = get_days_from_today(given_date)
print(f'{result} днів між сьогоднішньою датою і заданою.')