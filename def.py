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