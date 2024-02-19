class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name : {self.name}\nSpecies : {self.species}")


class Dog(Animal):
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        super().__init__(name,species="Dog")
    def show_details(self):
        super().show_details()
        print(f"Breed : {self.breed}")        


class Labrador(Dog):
    def __init__(self,name:str,color:str):
        self.name = name
        self.color = color
        super().__init__(name.capitalize(),breed="Labrador")
    def show_details(self):
        super().show_details()
        print(f"Color : {self.color}")


d = Labrador("tommy","Black")
d.show_details()
    