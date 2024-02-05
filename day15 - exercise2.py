import time

# timestamp = int(time.strftime("%H"))
timestamp = 12


if timestamp < 12 :
    print("Good Morning Sir.")
elif (timestamp < 15):
    print("Good Afternoon Sir.")
else:
    print("Good Evening Sir.")