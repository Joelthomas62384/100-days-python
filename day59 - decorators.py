

def greet(fn):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fn(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)

# hello()
# add(10,20)    
    

# greet(hello)()