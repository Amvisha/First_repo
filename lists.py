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