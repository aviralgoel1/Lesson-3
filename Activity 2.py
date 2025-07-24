#Electricity bill
while True:
    units=int(input("How many units did you consumer? "))
    if units <50:
        amount=units*2.6
        aftertax=amount+25
        print("You total bill will be "+str(aftertax)+" INR with"+str(aftertax-amount)+"tax")
    elif units <=100:
        amount=units*3.25
        aftertax=amount+35
        print("You total bill will be "+str(aftertax)+" INR with"+str(aftertax-amount)+"tax")
    elif units <=200:
        amount=units*6.26
        aftertax=amount+45
        print("You total bill will be "+str(aftertax)+" INR with"+str(aftertax-amount)+"tax")
    else:
        amount=units*8.45
        aftertax=amount+75
        print("You total bill will be "+str(aftertax)+" INR with"+str(aftertax-amount)+"tax")
