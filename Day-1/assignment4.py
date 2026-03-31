# Task 1: Greeting with name and age
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")

# Task 2: Temperature conversion from Celsius to Fahrenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.1f}")

# Task 3: Formatted receipt with 3 items
print("\n" + "="*40)
print("RECEIPT".center(40))
print("="*40)

total = 0
for i in range(1, 4):
    item_name = input(f"Enter item {i} name: ")
    item_price = float(input(f"Enter price for {item_name}: "))
    print(f"{item_name:<25} Rs.{item_price:>10.2f}")
    total += item_price

print("-"*40)
print(f"{'TOTAL':<25} Rs.{total:>10.2f}")
print("="*40)