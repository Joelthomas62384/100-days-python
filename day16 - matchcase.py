vote = (input("Do you want to vote"))


match vote:
    case 1:
        print("You can vote")
    case 2: 
        print("You cannot vote")
    case _ if vote == "1":
        print("You can vote")

    case _ if vote == "2":
        print("You cannot vote")


    case _ :
        print("You are an idiot")

print(type(vote))