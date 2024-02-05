letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Joel"
# print(letter.format(country,name))

price = 8.22524

letter = f"Hey my name is {name} and I am from {country} {price:.2f}"


letter = f"Hey my name is {{name}} and I am from {{country}} {price:.2f}" # double curly brackets to print the bracket

print(letter)

