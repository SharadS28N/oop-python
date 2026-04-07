class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs{amount}. Balance: Rs{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs{amount}. Balance: Rs{self.balance}")
        else:
            print("Insufficient funds.")

acc = BankAccount()
acc.deposit(500) 
acc.withdraw(200)
acc.withdraw(400)