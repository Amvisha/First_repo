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
