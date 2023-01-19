print("Auctioneer Game")

di = {}
while True:
    get = input("Do you want to bid, type yes or no") 
    if get == "yes":
        name = input("Enter your name")
        price = input("Enter your price")
        di[name] = price
    elif get == "no":
        break 
    else:
        print("Wrong Input")
    
    

res = max(di.values())
for i,j in di.items():
    if j == res:
        pritn(i,j)
        break 
