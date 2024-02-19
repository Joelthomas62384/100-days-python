class Employee:
    def __init__(self,name,salary):
        self.name  = name
        self.salary = salary

    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")


class Programmer(Employee):
    def showLanguage(self):
        print(f"The default language is Python")


Joel = Employee("Joel",100000)
Joel.showDetails()

e2 = Programmer("Jose",12341234)
e2.showDetails()
e2.showLanguage()