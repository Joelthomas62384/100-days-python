class Employee:
    companyName = "Apple"
    noofempl = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noofempl += 1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")
        print(f"Total number of employees is {self.noofempl}")



# Employee.showDetails(emp)

emp = Employee("Joel")
emp.raise_amount = 0.03
emp.showDetails()

emp2 = Employee("Jose")
emp2.showDetails()