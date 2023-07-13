#date :15/8/2021
#programmer : Frank

print("Welcome user.")
bill= float(input("Enter your total bill: "))
people=int(input("How many people do you want to share the bill with: "))
discount = int(input(r"choose a discount, 10% or 12% or 15%: "))
rem=(bill*discount)/100
output=(bill-rem)/people
#The formular in one line bill=(bill(1-(discount/100)))/people
print('You will each pay: $' + str(output))