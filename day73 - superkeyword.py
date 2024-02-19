class ParentClass:
    def parent_method(self):
        print("I am inside the child method of Parent Class")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Joel")
        super().parent_method()
    def child_method(self):
        print("I am inside the child method of the child Class")


    
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()
