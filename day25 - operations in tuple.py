numbers = (1,2,3,4,5,23,4)
numbers = list(numbers)
numbers.append(9000)
numbers.pop(0)
numbers[2] = "Joel"
numbers = tuple(numbers)

print(type(numbers),numbers)


# ------------------
print(numbers.index("Joel"))