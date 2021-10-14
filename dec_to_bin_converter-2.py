#date :15/8/2021
#programmer : Frank

bin=""
num = int(input("Enter an integer: "))
while num!=0:
    rem = num % 2
    num = num // 2
    bin += str(rem) 
print(bin[::-1])
