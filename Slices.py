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
print(result)  # Виведе: 15"""

def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]


