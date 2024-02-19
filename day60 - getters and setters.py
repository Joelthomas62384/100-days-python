class Myclass:
    def __init__(self,value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value} ")

    @property
    def Ten_value(self):
        return self._value *10
    
    @Ten_value.setter
    def Ten_value(self,newval):
        self._value = newval/10
    


obj = Myclass(10)
obj.Ten_value = 67
print(obj.Ten_value)
obj.show()




