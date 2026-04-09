class Employee:
	company = "TechCorp"  # class variable
	employee_count = 0     # class variable to count created objects

	def __init__(self, name, role):
		self.name = name   # instance variable
		self.role = role   # instance variable
		Employee.employee_count += 1


# Create three employees
emp1 = Employee("Mingmar", "Developer")
emp2 = Employee("Arun", "Designer")
emp3 = Employee("Bimit", "Tester")

# Print each employee's company and name
print("Employee details:")
print(emp1.company, "-", emp1.name)
print(emp2.company, "-", emp2.name)
print(emp3.company, "-", emp3.name)

# Print total employee count
print("\nTotal employees created:", Employee.employee_count)


# Pitfall experiment: change class variable through one instance
obj1 = Employee("Heman", "Intern")
obj2 = Employee("Kastub", "Support")

print("\nBefore changing through instance:")
print("obj1.company:", obj1.company)
print("obj2.company:", obj2.company)
print("Employee.company:", Employee.company)

# This creates an instance variable on obj1, does NOT change class variable
obj1.company = "NewTech"

print("\nAfter changing obj1.company = 'NewTech':")
print("obj1.company:", obj1.company)
print("obj2.company:", obj2.company)
print("Employee.company:", Employee.company)

# If you want to change for all, change through class
Employee.company = "GlobalTech"

print("\nAfter changing Employee.company = 'GlobalTech':")
print("obj1.company:", obj1.company)  # still NewTech (instance variable)
print("obj2.company:", obj2.company)  # now GlobalTech
print("Employee.company:", Employee.company)
