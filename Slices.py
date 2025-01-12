"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2::3]
print(three_numbers)


num = int(input('Введіть ціле число:'))
if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0:
    print('Fizz')
else:
    print(num)

length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)

name = input("Your name? ")
email = input("Your email? ")
age = int(input("Your age? "))
height = float(input("Your height? "))
is_active = bool(input("Do you want to receive notifications from the site? "))
print(f'{name} {type(name)}, {email} {type(email)}, {age} {type(age)}, {height} {type(height)}, {is_active} {type(is_active)}.')

cat = {}
info = {"status": "vaccinated", "breed": True}
cat = {'nick': "Simon", "age": 7,"characteristics": ["лагідний", "кусається"]}
age = cat.get("age")
cat.update(info)
print(cat)


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True
print(a is c)  # False

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

val = 0
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


def add_numbers(num1: int, num2: int) -> int:
    sum = num1 * num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15

def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
    print("Кандидат проходить до наступного туру.")
else:
    is_next = False
    print("Кандидат не проходить до наступного туру.")

work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
    print(developer_type)
elif work_experience <= 1:
    developer_type = "Junior"
    print(developer_type)
else:
    developer_type = "Senior"
    print(developer_type)

num = int(input("Enter a number: "))

if num > 0:
    if not num % 2 == 0:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
print(result)

num = int(input("Enter the integer (0 to 100): "))
sum = 0
while num >= 0:
    sum += num
    num -= 1
print(sum)

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = ("e")
result = 0
for i in message:
    if i == search:
        result += 1
print(result)

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = int(pool / quantity)
except ZeroDivisionError:
    print('Divide by zero completed!')

def greeting():
    print ("Hello world!")
greeting()

def invite_to_event(username):
    return print(f"Dear {username}, we have the honour to invite you to our event")
invite_to_event("Степан")

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()
    return price

def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return print(f'{first_name} {middle_name} {last_name}')
    else:
        return print(f'{first_name} {last_name}')
get_fullname('first_name','last_name')

def format_string(string: str, length: int) -> str:
    if len(string) >= length:
        print(string)
        return string
    else:
        string = (" " * ((length - len(string)) // 2)) + string
        print(string)
        return string
format_string("string", 40)

def first(size, *args):
    return size + len(args)
def second(size, **kwargs):
    return size + len(kwargs)
print(first(5, "first", "second", "third"))  # Результат: 8
print(first(1, "Alex", "Boris"))             # Результат: 3
print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
print(second(10, comment_one="Alex", comment_two="Boris"))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
def number_of_groups(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))
number_of_groups(50, 7)

import datetime
now = datetime.datetime.now()
print(now)

from datetime import datetime
current_datetime = datetime.now()
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)
print(current_datetime.date())
print(current_datetime.time())

import datetime
# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)
# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)
print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
"""

import datetime
# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2025, month=1, day=12, hour=14, minute=30, second=15)
specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)
print(specific_date)
print(specific_datetime)
from datetime import datetime
# Створення об'єкта datetime
now = datetime.now()
# Отримання номера дня тижня
day_of_week = now.weekday()
# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)
# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

from datetime import datetime
seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0
from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)
from datetime import datetime, timedelta
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)
print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00
from datetime import datetime
# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)
# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")
from datetime import datetime
# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
# Поточна дата
current_date = datetime.now()
# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)
from datetime import datetime
# Поточний час
now = datetime.now()
# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу
from datetime import datetime
# Припустимо, є timestamp
timestamp = 1617183600
# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime



