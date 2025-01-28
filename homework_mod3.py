from datetime import datetime
def get_days_from_today(date: datetime) -> int:
    """
    Function returns an integer indicating the number of days from the given date to the current one

    Input:
    :param date: datetime

    Output:
    :return: integer
    """
    today = datetime.today()
    days_from_today = (given_date - today).days

    return days_from_today

given_date = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09') ")

while True:
    try:
        print(type(given_date))
        given_date = datetime.strptime(given_date, '%Y-%m-%d')
        print(type(given_date))
    except ValueError:
        print(f"{given_date} is not a number in format 'YYYY-MM-DD' (example, '2020-10-09'). Please write number in format 'YYYY-MM-DD'!")
    except TypeError:
        print(f"{given_date} is not a number in format 'YYYY-MM-DD' (example, '2020-10-09'). Please write number in format 'YYYY-MM-DD'!T")
    finally:
        print('.' * 60)
    break

result: int = get_days_from_today(given_date)
print(result, type(result))

"""    

 while True:
        given_date = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09') ")
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
