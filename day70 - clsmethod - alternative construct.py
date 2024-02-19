# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0], string.split("-")[1])



# string  = "John-1200000"
# e = Employee.fromstr(string)
# e = Employee()
# e.init(string)
# print(e.name)
# print(e.salary)


st = "welcome my friends"
rst = ""
for i in range(1,len(st)+1):
    rst += st[-i]
print(rst)

