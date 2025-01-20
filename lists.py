from pygame.draw import circle

my_list = [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]

"""print(my_list.index(347))
my_list.insert(my_list.index(347), 100000000)
print(my_list)
my_list[my_list.index(7)] = -99999999
print(my_list)
my_list[10] = None
print(type(my_list.clear()))
sorted_list = sorted(my_list.copy())
print(sorted_list)"""
#my_list.sort(reverse=True)

"""
print(my_list.count(347))
print(len(my_list))
print(my_list[::-1]) #[0, -23, -435, 347, 235, 235, 346, 7, 5, 3, 2, 1]
print(my_list[-1]) # 0
print(my_list[3:]) # [5, 7, 346, 235, 235, 347, -435, -23, 0]
print(my_list[:6]) # [1, 2, 3, 5, 7, 346]
print(my_list[2:10]) # [3, 5, 7, 346, 235, 235, 347, -435]
print(my_list[:6:-1]) # [0, -23, -435, 347, 235]
print(my_list[:]) # [1, 2, 3, 5, 7, 346, 235, 235, 347, -435, -23, 0]
print(my_list[2:10:2]) # [3, 7, 235, 347]

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
print(users[:]["birthday"]
"""
'''
my_set = {1, 2, 3, 56, 'test', 'Test'}
print(my_set)
my_set.add('fakell')
print(my_set)
my_set.remove('fakell')
print(my_set)
my_set.discard(2)
print(my_set)

list_one = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]
list_two = [11, 1, 21, 31, 15, 8, 13, 21, 21, 7, 15, 101]
print(list(set(list_one) & set(list_two))) # in fist and second & (and)
print(list(set(list_one) | set(list_two))) # in fist or in second | (or)
print(list(set(list_one) - set(list_two))) # in fist and not in second & (minus)
print(list(set(list_one) ^ set(list_two))) # in fist and not in second + in second and not in fist ^
list_one = [1, 1, 2, 3, 5, 8, 13]
list_two = [11, 1, 21, 31, 15, 8]
print(len(list_one) == len(set(list_one)))
print(len(list_two) == len(set(list_two)))

circle = {
    (0, 0): "Centre",
    (0, 1): "90",
    (1, 0): "0 or 360",
    (0, -1): "270",
    (-1, 0): "180",
}
print(circle.get((0, -1))).
'''

my_string = 'hello my LiTTle friends!'
print(my_string.upper()) # HELLO MY LITTLE FRIENDS!
print(my_string.lower()) # hello my little friends!
print(my_string.startswith('hello')) # True
print(my_string.startswith('hi')) # False
print(my_string.endswith('!')) # True
print(my_string.endswith('.')) # False
print(my_string.title()) # Hello My Little Friends!
print(my_string.count('e')) # 3
print(my_string.capitalize()) # Hello my little friends!


