def my_generator():
    lis = [1,2,34,5,3]
    for i in lis:
        yield i

gen = my_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)