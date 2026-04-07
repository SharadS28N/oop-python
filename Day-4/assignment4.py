class Book:
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages


book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

print(f"Book 1: {book1.title}, {book1.author}, {book1.pages} pages")
print(f"Book 2: {book2.title}, {book2.author}, {book2.pages} pages")


class Car:
	def __init__(self, color="White"):
		self.color = color


car1 = Car("Red")
car2 = Car()

print(f"Car 1 color: {car1.color}")
print(f"Car 2 color: {car2.color}")


class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height


rectangle = Rectangle(5, 3)
print(f"Rectangle area: {rectangle.area()}")
