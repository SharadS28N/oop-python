"""
Assignment 3 - File Handling and Exception Handling
Topics: File operations, try-except-finally blocks, input validation
"""

# ============================================================
# PART 1: File Handling Functions
# ============================================================

def create_file_with_content(filename, lines):
    """Create a file and write lines of text into it (write mode)"""
    try:
        with open(filename, 'w') as file:
            for i, line in enumerate(lines, 1):
                file.write(f"Line {i}: {line}\n")
        print(f"✓ File '{filename}' created successfully with {len(lines)} lines.")
    except Exception as e:
        print(f"✗ Error creating file: {e}")


def read_and_print_file(filename):
    """Open a file and print its contents"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\n📄 Contents of '{filename}':")
            print("-" * 40)
            print(content)
            print("-" * 40)
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found!")
    except PermissionError:
        print(f"✗ Error: Permission denied to read '{filename}'!")
    except Exception as e:
        print(f"✗ Error reading file: {e}")


def append_to_file(filename, new_content):
    """Add new content to an existing file without deleting old data (append mode)"""
    try:
        with open(filename, 'a') as file:
            file.write(f"\n{new_content}\n")
        print(f"✓ Content appended to '{filename}' successfully.")
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found!")
    except PermissionError:
        print(f"✗ Error: Permission denied to write to '{filename}'!")
    except Exception as e:
        print(f"✗ Error appending to file: {e}")


# ============================================================
# PART 2: Exception Handling Functions
# ============================================================

def safe_division(a, b):
    """Handle division by zero using try-except"""
    try:
        result = a / b
        print(f"✓ Result: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("✗ Error: Division by zero is not allowed!")
        return None
    except TypeError:
        print("✗ Error: Both inputs must be numbers!")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None


def get_numeric_input(prompt="Enter a number: "):
    """Take user input and handle cases where input is not a number"""
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            print(f"✓ Valid number entered: {number}")
            return number
        except ValueError:
            print("✗ Error: That's not a valid number! Please try again.")
        except KeyboardInterrupt:
            print("\n⚠ Input cancelled by user.")
            return None
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            return None


def demonstrate_finally_block():
    """Demonstrate use of finally block"""
    print("\n🔍 Demonstrating try-except-finally block:")
    print("-" * 40)
    
    file = None
    try:
        filename = "demo_temp.txt"
        file = open(filename, 'w')
        file.write("Testing finally block...\n")
        
        # Simulate an error
        result = 10 / 0
        
    except ZeroDivisionError:
        print("✗ Caught ZeroDivisionError!")
    except Exception as e:
        print(f"✗ Caught exception: {e}")
    finally:
        # This block ALWAYS executes, whether exception occurred or not
        print("✓ Finally block executed - cleaning up resources...")
        if file:
            file.close()
            print("✓ File closed successfully in finally block.")
        print("-" * 40)


# ============================================================
# PART 3: Main Program - Demonstration
# ============================================================

def main():
    """Main function to demonstrate all concepts"""
    print("=" * 60)
    print("ASSIGNMENT 3 - File Handling & Exception Handling")
    print("=" * 60)
    
    # Define the test file path
    test_file = "test_content.txt"
    
    # --- Task 1 & 2: Create file and write 5 lines ---
    print("\n📝 TASK 1 & 2: Create file and write 5 lines")
    print("-" * 40)
    five_lines = [
        "Hello, this is line one.",
        "Python file handling is powerful!",
        "We can read, write, and append files.",
        "Exception handling makes code robust.",
        "Finally blocks ensure cleanup happens."
    ]
    create_file_with_content(test_file, five_lines)
    
    # --- Task 3: Read and print file contents ---
    print("\n📖 TASK 3: Open file and print its contents")
    read_and_print_file(test_file)
    
    # --- Task 4: Append new content without deleting old data ---
    print("\n➕ TASK 4: Add new content to existing file (append)")
    new_content = "APPENDED: This line was added without deleting old data!"
    append_to_file(test_file, new_content)
    
    # Verify the append worked
    print("\n📖 Verifying appended content:")
    read_and_print_file(test_file)
    
    # --- Task 5: Division by zero handling ---
    print("\n🔢 TASK 5: Division with zero handling")
    print("-" * 40)
    safe_division(10, 2)      # Normal division
    safe_division(10, 0)      # Division by zero
    safe_division(10, "a")    # Type error
    
    # --- Task 6: User input validation ---
    print("\n⌨️  TASK 6: User input validation")
    print("-" * 40)
    print("(Try entering non-numbers like 'abc' to see error handling)")
    num1 = get_numeric_input("Enter first number: ")
    num2 = get_numeric_input("Enter second number: ")
    
    if num1 is not None and num2 is not None:
        print(f"\n✓ You entered: {num1} and {num2}")
        safe_division(num1, num2)
    
    # --- Task 7: Finally block demonstration ---
    print("\n🧹 TASK 7: Finally block demonstration")
    demonstrate_finally_block()
    
    # --- Cleanup ---
    print("\n✅ All tasks completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
