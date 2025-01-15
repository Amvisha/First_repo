"""
from datetime import datetime
def string_to_date(date_string):
    date_string = datetime.strptime(date_string, "%Y.%m.%d")
    return date_string.date()
def date_to_string(date):
    date = datetime.strftime(date, "%Y.%m.%d")
    return date
date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date_string = date_to_string(converted_date)
print(date_string)
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