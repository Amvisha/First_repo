"""
from datetime import datetime
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()
def date_to_string(date):
    return date.strftime(date, "%Y.%m.%d")
date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date_string = date_to_string(converted_date)
print(date_string)
"""

"""
from datetime import datetime
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()
def prepare_user_list(user_data):
    for user in user_data:
        user["birthday"] = string_to_date(user["birthday"])
    return user_data
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
prepared_users = prepare_user_list(users)
print(prepared_users)
"""


from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def find_next_weekday(start_date, weekday):
    if weekday <= start_date.weekday():
        days_ahead = weekday - start_date.weekday() + 7
    else:
        days_ahead = weekday - start_date.weekday()
    return start_date + timedelta(days=days_ahead)

start_date = string_to_date("1955.3.25")  # Перетворення рядка на дату
print()
print(f'Поточний день тижня: {start_date} {start_date.weekday()}')
next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
print(f'Наступний понеділок: {next_monday} {next_monday.weekday()}')

next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(f"Наступна п'ятниця: {next_friday} {next_friday.weekday()}")


"""
from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        if (user["birthday"] - today).days >= 0 and (user["birthday"] - today).days <= days:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(user["birthday"])})
    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
prepared_users = prepare_user_list(users)

#today = string_to_date("2024.04.22")
birthday_this_year = []
today = date.today()
for user in users:
    birthday_this_year.append({"name": user["name"], "birthday": string_to_date(user["birthday"]).replace(year=today.year)})

upcoming_birthdays = get_upcoming_birthdays(birthday_this_year, days=7)
print(upcoming_birthdays)
"""

"""
from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = datetime(year=2024, month=4, day=22).date()
    for user in users:
        if (user["birthday"] - today).days >= 0 & (user["birthday"] - today).days <= days:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(user["birthday"])})
    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.4.23"},
    {"name": "Steve Jobs", "birthday": "1955.4.25"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
prepared_users = prepare_user_list(users)

#today = string_to_date("2024.04.22")
birthday_this_year = []
today = datetime(year=2024, month=4, day=22).date()
print(today)
for user in users:
    birthday_this_year.append({"name": user["name"], "birthday": string_to_date(user["birthday"]).replace(year=2024)})

upcoming_birthdays = get_upcoming_birthdays(birthday_this_year, days=7)
print(upcoming_birthdays)
"""


from datetime import datetime, timedelta, date

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"]).replace(year=today.year)})
    return prepared_list

def find_next_weekday(start_date, weekday):
    if weekday <= start_date.weekday():
        days_ahead = weekday - start_date.weekday() + 7
    else:
        days_ahead = weekday - start_date.weekday()
    return start_date + timedelta(days=days_ahead)

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        if (user["birthday"] - today).days >= 0 and (user["birthday"] - today).days <= days:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(user["birthday"])})
    return upcoming_birthdays


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
birthday_this_year = prepare_user_list(users)

today = date.today()
for user in users:
    birthday_this_year.append(
        {"name": user["name"], "birthday": string_to_date(user["birthday"]).replace(year=today.year)})

print(get_upcoming_birthdays(birthday_this_year))

