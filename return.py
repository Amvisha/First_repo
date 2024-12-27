def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

n = int(input("Введіть число:"))
print(factorial(n)) # виведе 120
