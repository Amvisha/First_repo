"""

from datetime import datetime, timedelta


def next_working_day(date):
"""
#    Функція для визначення наступного робочого дня.
#    :param date: Дата
#    :return: Наступний робочий день
"""
    if date.weekday() == 5:  # Субота
        return date + timedelta(days=2)  # Понеділок
    elif date.weekday() == 6:  # Неділя
        return date + timedelta(days=1)  # Понеділок
    return date


def get_birthdays_within_week(users):
"""
#    Функція, яка повертає список користувачів, у яких день народження
#    протягом наступних 7 днів, включаючи сьогодні,
#    з урахуванням перенесення на наступний робочий день.
#
#    :param users: Список користувачів з іменами та днями народження
#    :return: Список імен користувачів з днями народження протягом тижня
"""
    today = datetime.now().date()
    week_from_today = today + timedelta(days=7)
    upcoming_birthdays = []
    
    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Визначаємо день народження цього року
        bday_this_year = bday.replace(year=today.year)
        
        if today <= bday_this_year <= week_from_today:
            # Переносимо на наступний робочий день, якщо потрібно
            greeting_day = next_working_day(bday_this_year)
            upcoming_birthdays.append({"name": user["name"], "greeting_day": greeting_day})

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_birthdays_within_week(users)

print("Колеги, яких потрібно привітати з днем народження:")
for user in upcoming_birthdays:
    print(f"{user['name']} - {user['greeting_day']}")
"""

from datetime import datetime, date, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def next_working_day(u_date):
    """
    Функція для визначення наступного робочого дня.
    :param u_date: Дата
    :return: Наступний робочий день
    """
    if u_date.weekday() == 5:  # Субота
        return u_date + timedelta(days=2)  # Понеділок
    elif u_date.weekday() == 6:  # Неділя
        return u_date + timedelta(days=1)  # Понеділок
    return u_date

def get_upcoming_birthdays(users_data, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user_data in users_data:
        #birthday = string_to_date(users_data)
        greeting_day = prepare_user_list(user_data).replace(year=today.year)
        if today <= users_data["birthday"] <= today + timedelta(days=7):

            upcoming_birthdays.append({"name": user["name"], "greeting_day": greeting_day})
    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Колеги, яких потрібно привітати з днем народження:")
for user in upcoming_birthdays:
    print(f"{user['name']} - {user['greeting_day']}")
