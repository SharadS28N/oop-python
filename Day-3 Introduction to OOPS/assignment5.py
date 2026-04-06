class Book:
	pass


book1 = Book()
book1.title = "The Alchemist"
book1.author = "Paulo Coelho"
book1.pages = 208

book2 = Book()
book2.title = "Atomic Habits"
book2.author = "James Clear"
book2.pages = 320

print("Book 1:")
print("Title:", book1.title)
print("Author:", book1.author)
print("Pages:", book1.pages)

print("Book 2:")
print("Title:", book2.title)
print("Author:", book2.author)
print("Pages:", book2.pages)


class Pet:
	pass


pet = Pet()
pet.name = "Buddy"
pet.age = 3

print("\nPet before update:")
print("Name:", pet.name)
print("Age:", pet.age)

pet.age = 4

print("Pet after update:")
print("Name:", pet.name)
print("Age:", pet.age)


class Product:
	pass


product1 = Product()
product1.name = "Notebook"
product1.price = 50
product1.quantity = 4

product2 = Product()
product2.name = "Pen"
product2.price = 10
product2.quantity = 12

print("\nProduct 1:")
print("Name:", product1.name)
print("Total value:", product1.price * product1.quantity)

print("Product 2:")
print("Name:", product2.name)
print("Total value:", product2.price * product2.quantity)
