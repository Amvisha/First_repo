"""
num = int(input("Enter the integer (0 to 100): "))
sum = 0
while num > 0:
    sum += num
    num -= 1

def invite_to_event(username):
    return print(f"Dear {username}, we have the honour to invite you to our event")
invite_to_event('Stepan')
user = 'Ivan'
print(f'{user[3]}')
invite_to_event(user)"""

import random
dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

import random
num = random.random()
print(num)

import random
fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

import random
print(random.randrange(10))  # Верхня межа є 10, але не включається

import random
target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

import random
cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}")

import random
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

import random
items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)

import random
colors = ['червоний', 'зелений', 'синій']
weights = [10, 100, 1000]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)

import random
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

import random
price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")

import math
# Вихідне число
x = 3.7
# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини
print(ceil_result, floor_result, trunc_result)

import math
# Використання констант
print(math.pi)  # Виведе приблизне значення π
# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута
# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9
# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2

s = "Hi there!"
start = 1
end = 10
print(s.find("er", start, end)) # 5
print(s.find("q")) # -1

s = 'Some words'
print(s.find("o"))
print(s.rfind('o'))

s = 'Some words'
print(s.index("o"))
print(s.rindex('o'))

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

clean = '   spacious   '.strip()
print(clean) # spacious

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)

text = "Hello, world!"
new_text = text.replace(", world", "")
print(new_text)

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "This is string example"
print(str.translate(trantab))

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
MAP = {}
for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c
result = "34 DF 56 AC".translate(MAP)
print(result)

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}
# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v
string = "Hello world"
result = ""
for ch in string:
    result = result + ch.upper().translate(table_morze_dict)
print(result)

for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total)

width = 5
for num in range(12):
    print(f'{num:^6} {num**2:^6} {num**3:^6}')

name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)
