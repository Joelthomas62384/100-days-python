class Employee:
    def __init__(self,):
        self.name = "Joel" # Public
        self.__age = 21 #Private



e = Employee()
print(e.name)
# print(e.__age ) # This will throw an error
print(e._Employee__age) # This will bring the private attribute outside and this is called name mangling
print(e.__dir__())
