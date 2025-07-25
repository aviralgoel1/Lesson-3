choice=int(input("Would you like a car (1) or a bike (2)?"))
if choice == 1:
    type = int(input("Would you like an SUV (1) or Sedan (2)?"))
    if type == 1:
        print("Please collect your SUV")
    elif type == 2:
        print("Please collect your Sedan")
    else:
        type = int(input("Please type SUV (1) or Sedan (2)"))  
elif choice == 2:
    type = int(input("Would you like an Standard (1) or Off-road (2)?"))
    if type == 1:
        print("Please collect your Standard bike")
    elif type == 2:
        print("Please collect your Off-road bike")
    else:
        type = int(input("Please type Standard or Off-road"))  