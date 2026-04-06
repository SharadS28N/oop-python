class Fruit:
	pass


fruit1 = Fruit()
fruit1.name = "Apple"

fruit2 = Fruit()
fruit2.name = "Banana"

fruit3 = Fruit()
fruit3.name = "Orange"

print("Fruits:")
print(fruit1.name)
print(fruit2.name)
print(fruit3.name)


class Phone:
	pass


phone1 = Phone()
phone2 = Phone()

print("\nPhone type checks:")
print(type(phone1))
print(type(phone2))
print(isinstance(phone1, Phone))
print(isinstance(phone2, Phone))


class Color:
	pass


color1 = Color()
color1.name = "Red"

color2 = Color()
color2.name = "Blue"

color2.name = "Green"

print("\nColors:")
print(color1.name)
print(color2.name)
