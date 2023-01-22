

dishes = ["Cappuccino","Latte","Espresso"]
machineWater = 300
machineCoffe = 300
machineMilk = 300

def checkContent():
    print("Water Remaining is", machineWater)
    print("Coffee Remaining is", machineCoffe)
    print("Milk Remaining is", machineMilk)


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
        if satisfied(inp):
            machineCoffe -= requirements[inp]["Coffee"]
            machineMilk -= requirements[inp]["Milk"] 
            machineWater -= requirements[inp]["Coffee"]

            print("Enjoy your Coffee. Thanks for visiting!")
            print(machineCoffe,machineMilk,machineWater)
    else:
        print("Wrong Input!")