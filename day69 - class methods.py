class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    @classmethod
    def changeCmpny(cls,newcom):
        cls.company = newcom



e1 = Employee()
e1.name = "Joel"
e1.changeCmpny("Tesla")
e1.show()
print(Employee.company)