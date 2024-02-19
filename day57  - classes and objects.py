class Person:
    name = "Joel"
    age = 21
    occupation = "Software Developer"
    net_worth = 1000

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.info()
a.name = "John"
a.occupation = "Accountant"
# print(a.name)
# print(a.occupation)
# print(a.net_worth)

a.info()

