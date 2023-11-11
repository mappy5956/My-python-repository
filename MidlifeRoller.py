bill=5
print("Enter your height:")
height=int(input())
if height > 120 :
    print("please enter the age")
    age=int(input())
    if age<12:
        print(f"your bill is ${bill}")
    elif age==12 and age<18:
        bill=+2
        print(f"Your bill is ${bill}")
    if age>18:
        bill+=7
        print(f"Your bill is ${bill}")
    if age==45 and age<=55:
        bill=0
        print("Your bill is ${bill}")
print("do you want a photograph enter Y or N:")
photo=input()
if photo=="Y":
    bill1=bill+3
print(f"Your final bill is ${bill1}")
