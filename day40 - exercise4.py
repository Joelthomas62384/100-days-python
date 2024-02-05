import string
import random

def encrypter(stringInput):
    random_string = string.ascii_letters + string.digits
    key = random.choice(['!', '@', '#', '$', '%',  '&', ])
    lis = []
    for i in stringInput.split(" "):
        if len(i)<=3:
            lis.append(i[::-1])
        else:
            prefix = ''.join(random.choice(random_string) for _ in range(3))
            suffix = ''.join(random.choice(random_string) for _ in range(3))
            lis.append(prefix + i[1:] + i[0] +suffix)
    return " ".join(lis).replace(" ",str(key)),str(key)

def decrypter(stringInput,key):
    lis = []
    for i in stringInput.split(key):
        if len(i)<=3:
            lis.append(i[::-1])
        else:
            st = i[3:-3] 
            lis.append(st[-1]+st[:-1])
    return " ".join(lis)
            
            
            

# x,key = encrypter("Enter he name of the person whom you love the most in your life")
# print(key,x)
print(decrypter("cEwnterEqXQ#eh#flJamenfSA#fo#eht#EpjersonpIlK#cMXhomwUmW#uoy#uheovelrgc#eht#tyrostmFiP#ni#hITourybMS#UK9ifelmVA","#"))
            





