# 1) Create a temprature class with a @property for celcius that rejectws values below -273.15 (Absolute Zero)
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = 0
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self._celsius = value
        else:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")

# 2) Create an Employee class with a read-only employee_id property and a settable salary property that only accepts positive values.       
class Employee:
    def __init__(self, employee_id, salary=0):
        self._employee_id = employee_id
        self._salary = 0
        self.salary = salary

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
        else:
            raise ValueError("Salary must be a positive value")
    
# 3) Create a rectangle class where width and height have setters (Positive values only) and area is a read-only compouted property.
class Rectangle:
    def __init__(self, width=1, height=1):
        self._width = 1
        self._height = 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive value")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive value")

    @property
    def area(self):
        return self._width * self._height
    
# Testing Temperature class
temp = Temperature(25)
print(temp.celsius)

# Testing Employee class
employee = Employee("E123", 50000)
print(employee.employee_id)
print(employee.salary)

# Testing Rectangle class
rect = Rectangle(4, 5)
print(rect.area)