def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result
print(concatenate("Hello ", "world", "!"))

import re
text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)
if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")

import re
text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Знайдено:", match.group())

import re
text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print("Електронна адреса:", match.group())

import re
email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)
if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)

import re
text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)
