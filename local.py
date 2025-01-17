"""def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)
price_bread = int(input("Вартість хліба: "))
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread, float(input("Знижка на хліб: ")))
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')
'"""

"""
name = ("Богдан")  # str
age = int(input("Введіть свій вік "))  # int
weight = 60.5  # float
is_student = input("Ви студент ? ")  # bool

print(f'Мене звати {name}. Мій вік - {age}. Моя вага {weight}. Я студент - {is_student}.')
"""
sentence = "The quick brown fox jumps over the lazy dog"
length_all = len(sentence)
print(f'Загальна довжина списку: {length_all}.')
for i in sentence:
    if i == " ":
        length_all = length_all - 1
print(f'Довжина без пробілів: {length_all}.')

