

dishes = ["Cappuccino","Latte","Espresso"]
machineWater = 300
machineCoffe = 300
machineMilk = 300
requirements = {}
requirements["Cappunccino"] = {"Water":100,"Milk":100,"Coffee":76,"Price":5}
requirements["Latte"] = {"Water":150,"Milk":75,"Coffee":52,"Price":4}
requirements["Espresso"] = {"Water":200,"Milk":0,"Coffee":100,"Price":2}

def checkContent():
    print("Water Remaining is", machineWater)
    print("Coffee Remaining is", machineCoffe)
    print("Milk Remaining is", machineMilk)

def costReq(choice):
    quarter = int(input("Enter the number of quarter coins")) * 0.25
    dime = int(input("Enter the number of dime coins")) * 0.10
    nickel = int(input("Enter the number of pnickel coins")) * 0.05
    penny = int(input("Enter the number of penny coins")) *0.01
    total = quarter + dime + nickel + penny 
    if total < requirements[choice]["Price"]:
        return False 
    else:
        print(f"Here is your change, ${total-requirements[choice]['Price']}")
        return True


requirements = {}
requirements["Cappunccino"] = {"Water":100,"Milk":100,"Coffee":76,"Price":5}
requirements["Latte"] = {"Water":150,"Milk":75,"Coffee":52,"Price":4}
requirements["Espresso"] = {"Water":200,"Milk":0,"Coffee":100,"Price":2}

def satisfied(inp):
    if (requirements[inp]["Water"] >=  machineWater):
        print("Not enough Water")
        return False
    elif (requirements[inp]["Milk"] >= machineMilk):
        print("Not enough Milk")
        return False 
    elif (requirements[inp]["Coffee"] >= machineCoffe):
        print("Not enouhg Coffee")
        return False 
    else:
        return True



inp = "Y"
while inp != "close":
    inp = input("Enter a command")
    if inp == "Report":
        checkContent()
    elif inp == "close":
        print("See you later, Bye!")
        continue
    elif inp in requirements:
        if costReq(inp):
            if satisfied(inp):
                machineCoffe -= requirements[inp]["Coffee"]
                machineMilk -= requirements[inp]["Milk"] 
                machineWater -= requirements[inp]["Coffee"]

                print("Enjoy your Coffee. Thanks for visiting!")
                print(machineCoffe,machineMilk,machineWater)
            else:
                print("Shortage of resources!")
        else:
            print('Shortage of Money!')
    else:
        print("Wrong Input!")