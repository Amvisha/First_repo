"""from itertools import count

counter = 0
while True:
    user_input = input('>>> ')
    counter += 1
    if user_input == 'exit' or counter >= 5:
        break
    else:
        print(f'You write: {user_input}')

lists = [1, 2, 'test text', 4, 5, 6, 7]
for i in lists:
    print(i)

for i in range(len(lists)):
    print(i, lists[i])"""

string_one = input('Enter string: ')
string_two = input('Enter string for compare: ')
for char in string_one:
    if char not in string_two:
        print(False)
        break
else:
    print(True)
















