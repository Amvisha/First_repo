def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)
    lst.append(5)
    print(lst)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]
