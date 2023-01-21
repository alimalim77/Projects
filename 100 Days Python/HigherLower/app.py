from data import data
import random

def pickerFunction():
    #User Input
    B = A = random.choice(data)

    #System Input
    while A == B:
        B = random.choice(data)
    return A,B

def rePicker(A):
    B = random.choice(data)
    while B == A:
        B = random.choice(data)
    return B

    

score = 0 
a,b = None,None
while True:
    if not a:
        a,b = pickerFunction()
    else:
        b = rePicker(a)
    print(f"{a['name']} has {a['follower_count']} followers")
    print(f"{b['name']} has {b['follower_count']} followers")
    
    user = input(("Who do you think is more popular? A or B?"))
    if user == "A" or user == "a":
        user = a
        comp = b
    elif user == "B" or user == "b":
        user = b 
        comp = a 
    else:
        print("Wrong Input ")
        break 

    if user["follower_count"] > comp["follower_count"]:
        score += 1 
        a = user
    else:
        print("You lost")
        print(f"Score was {score}")
        break
    

