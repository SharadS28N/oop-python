class Greeter:
	def __init__(self, name):
		self.name = name

	def greet(self):
		print(f"Hello, my name is {self.name}!")


class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height


class BankAccount:
	def __init__(self, balance):
		self.balance = balance

	def check_balance(self):
		print(self.balance)

greeter = Greeter("Abishek Magar")
greeter.greet()

rectangle = Rectangle(5, 3)
print("Area of rectangle:", rectangle.area())

account = BankAccount(1000)
account.check_balance()
account.balance += 500
account.check_balance()