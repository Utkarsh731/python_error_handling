class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise MyCustomError("Age cannot be negative.")
except MyCustomError as e:
    print(e)
else:
    print("Valid age entered.")
