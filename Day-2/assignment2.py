# 1) function is_even(number) that returns true if the number is even and false otherwise
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True

# 2) function calculate_area(length, width) that returns the area of 3 different rectangles
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))  # 15

# 3) function create_receipt(item, price, quantity)
def create_receipt(item, price, quantity):
    total = price * quantity
    return f"Item: {item}, Price: Rs{price}, Quantity: {quantity}, Total: Rs{total}"

print(create_receipt("Book", 200, 3))  # Item: Book, Price: Rs200, Quantity: 3, Total: Rs600