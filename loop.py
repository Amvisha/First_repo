from itertools import count

counter = 0
while True:
    user_input = input('>>> ')
    counter += 1
    if user_input == 'exit' or counter >= 5:
        break
    else:
        print(f'You write: {user_input}')