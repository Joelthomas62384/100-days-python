class Employee:
    def __init__(self,name) -> None:
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance) -> None:
        self.dance = dance
    
    def show(self):
        print(f"The dance is {self.dance}")
    

class EmployeeDancer(Employee,Dancer):
    def __init__(self,name,dance) -> None:
        self.name = name
        self.dance = dance
    def show(self):
        Employee.show(self)
        Dancer.show(self)


o = EmployeeDancer("Joel","Katak")
# print(o.name,o.dance)
o.show()
# print(EmployeeDancer.mro())