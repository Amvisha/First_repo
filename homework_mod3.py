from datetime import datetime

def get_days_from_today() -> int:
    """
    Function returns an integer indicating the number of days from the given date to the current one

    Output:
    :return: integer
             A negative number if the specified date is in the future.
    """
    while True:
        given_date = input("Enter the date in the format 'YYYY-MM-DD' (e.g. '2020-10-09') ")

        try:
            given_date = datetime.strptime(given_date, '%Y-%m-%d').date()  # Converting a date string to a datetime object
            break

        except Exception as e:
            print(e)

        #    print(f"Time data {given_date} does not match format 'YYYY-MM-DD' (e.g. '2020-10-09'). Please write number in format 'YYYY-MM-DD'!")
    today = datetime.today().date()  # Current date
    days_from_today = (given_date - today).days  # Difference between dates
    return days_from_today

result: int = get_days_from_today()
print(f"{result} days between today's date and the given date.")

"""    

 while True:
        given_date = input("Enter the date in the format 'YYYY-MM-DD' (e.g. '2020-10-09') ")
        try:
            given_date = datetime.strptime(given_date, '%Y-%m-%d').date()
            if age >= 18:
                print(get_days_from_today(given_date))
                break
            else:
                print('Access denied')
                break
        except ValueError:
            print(f"{given_date} is not a number in format 'YYYY-MM-DD' (example, '2020-10-09'). Please write number in format 'YYYY-MM-DD'!")
        finally:
            print('.' * 60)
"""



#def add(value_one: int, value_two: int) ->int:
"""
    Function of adding two numbers

    Input:
    :param value_one: integer
    :param value_two: integer

    Output:
    :return: integer
"""
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
"""
