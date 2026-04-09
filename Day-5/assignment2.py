class Password:
	def __init__(self, password):
		self.__password = password

	def check_password(self, guess):
		return guess == self.__password


class Temperature:
	def __init__(self, celsius=0):
		self.__celsius = 0
		self.set_temperature(celsius)

	def set_temperature(self, celsius):
		if -273.15 <= celsius <= 1000:
			self.__celsius = celsius
			return True
		return False

	def get_temperature(self):
		return self.__celsius


class BankAccount:
	def __init__(self, balance=0):
		self.__balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			return True
		return False

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			return True
		return False

	def get_balance(self):
		return self.__balance
	
# Testing Password class
password = Password("secret123")
print(password.check_password("secret123"))  # True
print(password.check_password("wrong"))     # False

# Testing Temperature class
temp = Temperature(25)
print(temp.get_temperature())  # 25
temp.set_temperature(-300)     # Invalid, should not change
print(temp.get_temperature())  # Still 25
temp.set_temperature(100)     # Valid
print(temp.get_temperature())  # 100

# Testing BankAccount class
account = BankAccount(100)
print(account.get_balance())  # 100
account.deposit(50)
print(account.get_balance())  # 150
account.withdraw(30)
print(account.get_balance())  # 120
account.withdraw(200)  # Invalid, should not change