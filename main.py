class Greeter:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привет, {self.name} ")

user = input("Как тебя зовут?")
greeter = Greeter(user)

greeter.say_hello()

