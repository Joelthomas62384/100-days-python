# num = input("Enter a number : ")

# try:
#     for i in range(1,11 ):
#         print(f"{i} x {int(num)} = {i*int(num)}")
# except Exception as e:
#     print(f"Invalid input")
    

# print("Some important lines of code")
# print("End of programme")




try:
    num = int(input("Enter a number : "))
    a = [1,3,5]
    print(a[num])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index Error")


