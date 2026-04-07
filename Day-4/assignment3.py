class Greeter:
	def greet(self, name):
		print(f"Hello, my name is {name}!")


class Rectangle:
	def area(self, width, height):
		return width * height


class BankAccount:
	def check_balance(self, balance):
		print(balance)

greeter = Greeter()
greeter.greet("Abishek Magar")

rectangle = Rectangle()
print("Area of rectangle:", rectangle.area(5, 3))

account = BankAccount()
account.check_balance(1000)
account.check_balance(1500)