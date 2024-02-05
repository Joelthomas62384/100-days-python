# Ningalkum Aavam Koodeeshwaran
from random import shuffle
options_ind = ["a","b","c","d"]
question_answers = [
    ["Which is the best programming language for AI?",["Python","Java","Kotlin","C"],0],
    ["Which is the best programming language for AI?",["Python","Java","Kotlin","C"],0],
    ["Which is the best programming language for AI?",["Python","Java","Kotlin","C"],0],
    ["Which is the best programming language for AI?",["Python","Java","Kotlin","C"],0],
    ["Which is the best programming language for AI?",["Python","Java","Kotlin","C"],0],
    ["Which is the longest venomous snake in the world?",["Python","King Cobra","Black Mamba","Russels Viper"],1],
    ["Which is the longest venomous snake in the world?",["Python","King Cobra","Black Mamba","Russels Viper"],1],
    ["Which is the longest venomous snake in the world?",["Python","King Cobra","Black Mamba","Russels Viper"],1],
    ["Which is the longest venomous snake in the world?",["Python","King Cobra","Black Mamba","Russels Viper"],1],
    ["Which is the longest venomous snake in the world?",["Python","King Cobra","Black Mamba","Russels Viper"],1],
    ["Who is the Prime Minister of India",["Modi","Amit Shah","Rahul Gandhi","Joel Thomas"],0],   
    ["Who is the Prime Minister of India",["Modi","Amit Shah","Rahul Gandhi","Joel Thomas"],0],   
    ["Who is the Prime Minister of India",["Modi","Amit Shah","Rahul Gandhi","Joel Thomas"],0],   
    ["Who is the Prime Minister of India",["Modi","Amit Shah","Rahul Gandhi","Joel Thomas"],0],   
    ["Who is the Prime Minister of India",["Modi","Amit Shah","Rahul Gandhi","Joel Thomas"],0],   
]


score_prices = [1000,2000,3000,5000,10000,30000,50000,750000,100000,500000,1000000,1500000,3000000,500000,10000000]
score = 0


for id, question in enumerate(question_answers, start=1):
    print(f"{id} {question[0]}")
    
    options = question[1].copy()
    shuffle(options)

    for index, option in enumerate(zip(options, options_ind),start=1):
        print(f"{options_ind[index-1]}. {option[0]}", end= "\t" if index%2!=0  else "\n")
    answer = input("Enter your answer : ")
  
    print("\n")
    if options[options_ind.index(answer)] == question[1][question[2]]:
        score += score_prices[id-1]
        print(f"You got {score_prices[id-1]} Rupees".center(100," "))
    elif answer == "q":
        print(f"You got ₹{score}".center(50,"-"))
        break
    else:
        print(f"Wrong Answer and the right answer is {question[1][question[2]]:}")
        if id<5:
            print(f"You did not get any money as you have failed to aquire the first safe position")
        elif id<9:
            score = 50000
            print(f"You got ₹{score}".center(50,"-"))
        elif id<12:
            score = 100000
            print(f"You got ₹{score} ".center(50,"-"))
        else:
            score = 3000000
            print(f"You got ₹{score} ".center(50,"-"))
        break
    print("\n")