# 1. Extend the BankAccount class with a transfer(other_account, amount) method that withdraws from one account and deposits into another.
# 2. Create a Library class that has a private list of books. Add methods to add a book,remove a book, and search by title. The book list should never be directly accessible.
# 3. Create an Inventory class with private stock counts per item. Add methods to add stock,sell items (with validation that stock does not go below zero), and a read-only property for total items in stock.

# 1. BankAccount class with transfer method
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def transfer(self, other_account, amount):
        if 0 < amount <= self._balance:
            self.withdraw(amount)
            other_account.deposit(amount)

    @property
    def balance(self):
        return self._balance
    
# 2. Library class with private list of books
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        self._books.append(title)

    def remove_book(self, title):
        if title in self._books:
            self._books.remove(title)

    def search_by_title(self, title):
        return title in self._books
    
# 3. Inventory class with private stock counts
class Inventory:
    def __init__(self):
        self._stock = {}

    def add_stock(self, item, quantity):
        if item in self._stock:
            self._stock[item] += quantity
        else:
            self._stock[item] = quantity

    def sell_item(self, item, quantity):
        if item in self._stock and self._stock[item] >= quantity:
            self._stock[item] -= quantity

    @property
    def total_items_in_stock(self):
        return sum(self._stock.values())
    
# Example usage:
# BankAccount
account1 = BankAccount(100)
account2 = BankAccount(50)
account1.transfer(account2, 30)
print(account1.balance)

# Library
library = Library()
library.add_book("The Great Gatsby")
print(library.search_by_title("The Great Gatsby"))
library.remove_book("The Great Gatsby")
print(library.search_by_title("The Great Gatsby"))

# Inventory
inventory = Inventory()
inventory.add_stock("Widget", 10)
inventory.sell_item("Widget", 3)
print(inventory.total_items_in_stock)