# Task 1: Arithmetic Operators
print("=== Task 1: Arithmetic Operators ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")

# Task 2: Tip Calculator
print("\n=== Task 2: Tip Calculator ===")
bill_amount = float(input("Enter bill amount: Rs."))
tip_percentage = float(input("Enter tip percentage: "))

tip = bill_amount * (tip_percentage / 100)
total = bill_amount + tip

print(f"Bill Amount: ${bill_amount:.2f}")
print(f"Tip ({tip_percentage}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")

# Task 3: Check Even or Odd
print("\n=== Task 3: Even or Odd ===")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")