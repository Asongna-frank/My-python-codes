#date :8/8/2021
#programmer : Frank

cel=float(input("Enter a celcius temperature:"))
farh=(9/5)*(cel+32)
print("The temperature in farhenheit is:",farh)
#OR
farh= (9/5)*(float(input("Enter a celcius temperature:")) + 32)
print("The temperature in farhenheit is:",farh)
print("The temperature in farhenheit is:",round(farh,3))

"""the "round( , )" function takes two parameters:
-The first is for the number to be rounded
-The second is the number of decimal places to be rounded """

a=5.4729
print(round(a,3)) 