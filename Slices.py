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
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
