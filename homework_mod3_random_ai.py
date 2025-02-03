import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
  """
  Генерує набір унікальних випадкових чисел для лотерейного квитка.

  Args:
    min: Мінімальне можливе число у наборі (не менше 1).
    max: Максимальне можливе число у наборі (не більше 1000).
    quantity: Кількість чисел, які потрібно вибрати (значення між min і max).

  Returns:
    Список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися.
    Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
  """

  # Перевірка валідності вхідних даних
  if not 1 <= min <= max <= 1000 or not min <= quantity <= max:
    return []

  # Генерація унікальних чисел
  numbers = set()
  while len(numbers) < quantity:
    numbers.add(random.randint(min, max))

  # Повернення відсортованого списку
  return sorted(list(numbers))

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 6, 6)
print("Ваші лотерейні числа:", lottery_numbers)