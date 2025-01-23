def add(value_one: int, value_two: int) ->int:
    """
    Function of adding two numbers

    Input:
    :param value_one: integer
    :param value_two: integer

    Output:
    :return: integer
    """
    sum_of_two_numbers = value_one + value_two
    return  sum_of_two_numbers

result: int = add(2, 4)
print(result)

def sum_of_all_numbers(*numbers): # *args -> (1,2,3,4,5,6,7,8,9)
    sum = 0
    for value in numbers:
        try:
            sum += value
        except TypeError:
            continue
        except ValueError:
            continue
    return sum
print(sum_of_all_numbers(1,2,3,4,5,6,7,8,9))




