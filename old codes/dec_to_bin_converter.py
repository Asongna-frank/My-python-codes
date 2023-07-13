#date :8/8/2021
#programmer : Frank

bin=[]
num = int(input("Enter an integer: "))
while num!=0:
    rem = num % 2
    num = num // 2
    bin.append(rem)
else:
    bin.reverse()
    print(bin)
