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

"""    

 while True:
        given_date = input("Enter the date in the format 'YYYY-MM-DD' (e.g. '2020-10-09') ")
        try:
            given_date = datetime.strptime(given_date, '%Y-%m-%d').date()
            if age >= 18:
                print(get_days_from_today(given_date))
                break
            else:
                print('Access denied')
                break
        except ValueError:
            print(f"{given_date} is not a number in format 'YYYY-MM-DD' (example, '2020-10-09'). Please write number in format 'YYYY-MM-DD'!")
        finally:
            print('.' * 60)
"""



#def add(value_one: int, value_two: int) ->int:
"""
    Function of adding two numbers

    Input:
    :param value_one: integer
    :param value_two: integer

    Output:
    :return: integer
"""
"""
    sum_of_two_numbers = value_one + value_two
    return  sum_of_two_numbers

result: int = add(2, 4)
print(result)

def sum_of_all_numbers(*numbers): # *args -> (1,2,3,4,5,6,7,8,9)
    sum = 0
    for value in numbers:
        try:
            sum += value
        except TypeError:
            continue
        except ValueError:
            continue
    return sum
print(sum_of_all_numbers(1,2,3,4,5,6,7,8,9))
"""
