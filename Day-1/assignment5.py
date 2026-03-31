# 1) Ask the user for a number. Print whether it is positive, negative or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2) Write a grading system, take a score (0-100) and print the letter grade (A, B, C, D, F).
score = float(input("Enter your score (0-100): "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# 3) Ask for an age and print the ticket price (Child under 12 :  $5, Adult 12-64 : $10, Senior 65+ : $7).
age = int(input("Enter your age: "))
if age < 12:
    price = 5
elif age < 65:
    price = 10
else:
    price = 7
print(f"Your ticket price is: ${price}")