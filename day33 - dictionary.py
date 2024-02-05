dic = {
    "name":"Joel Thomas",
    "age":21,
    "Location":"Kerala",
    "Gender":"Male",
    "Salary":"52000"
}

# print(dic['age'])
# print(dic.get("name",""))
    
# for key in dic.keys():
#     print(f"{key} : {dic[key]}")


for key , item in dic.items():
    print(f"{key} : {item}")