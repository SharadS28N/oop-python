class Dog:
    name = "Buddy"
    breed = "Golden Retriever"
    sound = "Woof"

    def noise(self, sound):
        print(f"{self.name} is making {sound} sound.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

dog1 = Dog()
dog1.name = "Max"
dog1.noise("bark")
dog1.eat("Sausage")

dog2 = Dog()
dog2.name = "Charlie"
dog2.noise("woof")
dog2.eat("Pedigree")
