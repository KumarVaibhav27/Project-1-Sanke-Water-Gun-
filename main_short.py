import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1,"g":0}
reverseDict = {1:"Snake", -1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer==you):
    print("Match is Draw")
else:    
    if(computer - you) == -1 or (computer - you) == 2:
        print("You LOSSEEE")
    else:
        print("You WIN!!")