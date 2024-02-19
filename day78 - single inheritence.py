class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!!!")

d = Dog("Jose","Lab")
d.make_sound()

a = Animal("Lion","Carnivorous")
a.make_sound()
        


        