marks= [12,3,98,43,12,3,67,4,7,45]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index==2):
#         print("Awesome Joel")
#     index+=1



for index, mark in enumerate(marks,1):
    print(index,mark)
    if (index==2):
        print("Awesome Joel")
