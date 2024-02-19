class Person:
    def __init__(self,n,c) :
        # print("Hey i am a person")
        self.name = n
        self.occ = c

        

    def info(self):
        print(f"{self.name} is a {self.occ}")



a = Person("Joel","Software Developer")
b = Person("Divya","Hr")

a.info()
b.info( )