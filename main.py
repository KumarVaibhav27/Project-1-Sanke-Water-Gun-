'''
1 for snake
-1 for water
0 for gun
'''
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
    if(computer==-1 and you==1):  # -2
        print("You WIN!!")
    elif(computer==-1 and you==0): # -1
        print("You LOSEEE!!")
    elif(computer==1 and you==-1): # 2
        print("You LOSEEE!!")
    elif(computer==1 and you==0):  # 1
        print("You WIN!!")
    elif(computer==0 and you==1):  # -1
        print("You LOSEEE!!")
    elif(computer==0 and you==-1):   #1
        print("You WIN!!")
    else:
        print("Something went wrong!!")