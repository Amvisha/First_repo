#def modify_list(lst: list) -> None:
#    lst = lst.copy()
#   lst.append(4)
#   lst.append(5)
#   print(lst)
#
#my_list = [1, 2, 3]
#modify_list(my_list)
#print(my_list)  # виведе: [1, 2, 3]
#hello =  'Hello'
#world = 'World'
#message = 'Write %s %s' % (hello, world)
#print(message)

#hello =  'Hello'
#world = 'World'
#message = 'Write {} {}'.format(hello, world)
#print(message)
"""
age = str(27.95)
message = round(float(age), 2), type(age)
print(message)

value_one = 5
value_two = 7
value_three = -19
summary = 0
summary += abs(value_one)
print(summary)
summary += abs(value_two)
print(summary)
summary += abs(value_three)
print(summary)

sentense_one = 'Hello world'
sentense_two = 'Hello ' + 'world'
print(sentense_one, sentense_two, sep='\n')
print(f'Are sentence equal?',  sentense_one == sentense_two)
print(f'Are sentence identical?',  sentense_one is sentense_two)
print(f'Path the sentence in memory {id(sentense_one)}')
print(f'Path the sentence in memory', id(sentense_two))
"""

flats = int(input('How many flats on the floor: '))
floors = int(input('How many floors in entrance: '))
flat_number = int(input('Enter flat number: '))
floor_number = 1
entrance = 1
while flat_number > flats:
    flat_number -= flats
    floor_number += 1
    if floor_number > floors:
        floor_number = 1
        entrance += 1
if flat_number <= 0:
    print(f'Wrong flat number {flat_number}.')
else:
    print(f'Flat in a {floor_number} floor in {entrance} entrance.')
"""

flat = int(input('How many flats on the floor: '))
floor = int(input('How many floors in entrance: '))
flat_number = int(input('Enter flat number: '))
flats_per_entrance = flat * floor
entrance_number = (flat_number - 1) // flats_per_entrance + 1
floor_number = ((flat_number - 1) % flats_per_entrance) // flat + 1
print(f'Flat in a {floor_number} floor in {entrance_number} entrance.')



if flat_number / 4 < 1 :
    floor = 1
    print(f'Flat in a {floor}')
else:
    for flat_number
"""
