from datetime import datetime, timedelta

# Список користувачів з їхніми днями народження
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.28"}
]


def get_upcoming_birthdays(users):
    today = datetime.now()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        # Встановлюємо рік народження на поточний
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув в цьому році, перевстановлюємо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження відбудеться в найближчі 7 днів
        if today <= birthday_this_year <= today + timedelta(days=7):
            upcoming_birthdays.append({"name": user["name"], "greeting_day": birthday_this_year})

    return upcoming_birthdays


# Викликаємо функцію та виводимо результат
#upcoming = get_upcoming_birthdays(users)
#print("Колеги, яких потрібно привітати з днем народження:")
#for name in upcoming:
#    print(name)

upcoming_birthdays = get_upcoming_birthdays(users)

print("Колеги, яких потрібно привітати з днем народження:")
for user in upcoming_birthdays:
    print(f"{user['name']} - {user['greeting_day'].date()}")