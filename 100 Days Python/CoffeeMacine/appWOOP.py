
class Requirements:
    def __init__(self,milk,water,coffee,cost= 5):
        self.milk = milk 
        self.water = water 
        self.coffee = coffee 
        self.cost = cost
    
    def refill(self):
        self.water = self.coffee = self.milk = 300
    
    def printReq(self):
        print("Milk is",self.milk)
        print("Water is",self.water)
        print("Coffee is",self.coffee)

class Money: 
    def __init__(self):
        self.quarter = 0
        self.dime = 0
        self.nickel = 0
        self.penny = 0
    
    def takeCash(self):
        self.quarter = int(input("Enter the number of quarter coins")) * 0.25
        self.dime = int(input("Enter the number of dime coins")) * 0.10
        self.nickel = int(input("Enter the number of pnickel coins")) * 0.05
        self.penny = int(input("Enter the number of penny coins")) *0.01
        self.total = self.quarter + self.dime + self.nickel + self.penny 
    
    def checkCash(self,drinkPrice):
        if self.total >= drinkPrice:
            print(f"Your change is {self.total-drinkPrice}")
            return True  
        else:
            print("Cash is insufficient")
            return False

    
#Declare Dishes
Cappuccino =  Requirements(100,76,100, 5)
Latte = Requirements(75, 150, 52, 4)
Espresso = Requirements(0, 200, 100, 2)

#Set Machine Requirements
Machine = Requirements(300, 300, 300)

def checkContent(cappucino,machine):
    if (cappucino.water >=  machine.water):
        print("Not enough Water")
        return False
    elif (cappucino.milk >=  machine.milk):
        print("Not enough Milk")
        return False 
    elif (cappucino.coffee >=  machine.coffee):
        print("Not enouhg Coffee")
        return False 
    else:
        return True

def deductAmount(Machine,Drink):
    Machine.coffee -= Drink.coffee
    Machine.water -= Drink.water
    Machine.milk -= Drink.milk

while True:
    want = input("Enter the order: ")
    if want =="quit":
        break
    if want == "Cappuccino".lower():
        if checkContent(Cappuccino,Machine):
            money = Money()
            money.takeCash()
            if money.checkCash(Cappuccino.cost):
                deductAmount(Machine, Cappuccino)
                rint("Here is your Cappuccino")
            

    elif want == "Latte".lower():
        if checkContent(Latte, Machine):
            money = Money()
            money.takeCash()
            if money.checkCash(Latte.cost):
                deductAmount(Machine, Latte)
                rint("Here is your Latte")
    elif want == "Espresso".lower():
        if checkContent(Espresso, Machine):
            money = Money()
            money.takeCash()
            if money.checkCash(Espresso.cost):
                deductAmount(Machine, Espresso)
                print("Here is your Espresso")



