# 1) Create one variable of each type and print with type()
my_int = 42
my_float = 3.14
my_str = "Hello"
my_bool = True

print(f"Integer: {my_int}, Type: {type(my_int)}")
print(f"Float: {my_float}, Type: {type(my_float)}")
print(f"String: {my_str}, Type: {type(my_str)}")
print(f"Boolean: {my_bool}, Type: {type(my_bool)}")

# 2) Convert string "100" to integer and add 50
string_num = "100"
result = int(string_num) + 50
print(f"\nString '100' converted to int + 50 = {result}")

# 3) Create a list of fruits and a dictionary with name and age
fruits = ["Apple", "Banana", "Orange"]
person = {"name": "John", "age": 25}

print(f"\nFruits: {fruits}")
print(f"Person: {person}")