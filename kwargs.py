def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", sex="man", age=25, destination=input("Місце призначення: "))
