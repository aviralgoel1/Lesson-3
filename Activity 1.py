medical=input("Did you have a medical cause. Type Y or N")
attendance=int(input("student attendance: "))
if medical == "Y":
    print("you can sit the exam")
else:
    if attendance >= 75:
        print("you can sit the exam")
    else:
        print("you cannot sit the exam")
