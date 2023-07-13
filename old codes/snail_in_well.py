#date :12/10/2021
#programmer : Frank

depth =int( input("Enter a depth "))
climb = 0
days= 0
while climb < depth :
    climb=climb+7
    print("climb after addition "+str(climb))
    if climb<depth:
        climb=climb-2
        print("climb after subtraction "+str(climb))
    days=days+1
    print(days)
    