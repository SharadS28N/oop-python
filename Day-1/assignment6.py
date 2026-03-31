# 1) Username and Passowrd "Access Granted"
def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    correct_username = "admin"
    correct_password = "password123"
    
    if username == correct_username and password == correct_password:
        print("Access Granted!")
    else:
        print("Invalid username or password!")

# 2) Check if number is between 1 and 100 (inclusive)
def check_range():
    number = int(input("Enter a number: "))
    
    if number >= 1 and number <= 100:
        print(f"{number} is between 1 and 100")
    else:
        print(f"{number} is NOT between 1 and 100")

# 3) Check if year is leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")

# Main menu
if __name__ == "__main__":
    while True:
        print("\n1. Login System")
        print("2. Check Number Range (1-100)")
        print("3. Check Leap Year")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            login_system()
        elif choice == "2":
            check_range()
        elif choice == "3":
            check_leap_year()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")