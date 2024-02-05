class CustomError(Exception):
    pass



a = (input("Enter any value between 5 and 9 : "))
if str(a) == 'quit'or int(a) <5 or int(a) > 9 :
    raise CustomError("Value should be between 5 and 9")
