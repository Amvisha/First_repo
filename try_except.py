"""

while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("Access allowed")
            break
        else:
            print('Access denied')
            break
    except ValueError:
        print(f'{age} is not a number. Please write number!')
    finally:
        print('.'*60)
"""

import datetime

def get_days_from_today(date):
  """
  Розраховує кількість днів між заданою датою і поточною датою.

  Args:
    date: Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'.

  Returns:
    Ціле число, яке вказує на кількість днів від заданої дати до поточної.
  """
  try:
    given_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    today = datetime.date.today()
    return (today - given_date).days
  except ValueError:
    print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
    return None

# Приклад використання:
date = "2021-10-09"
days_difference = get_days_from_today(date)
print(f"Кількість днів від {date} до сьогодні: {days_difference}")