#date :12/9/2021
#programmer : Frank

def intro(fname,lname):
    print(f"my name is {fname} {lname}")
    # OR print(f"my name is %s %s "%(fname,lname))
print(intro("mark","davis"))

def mult(*args):
#the "*" before "args" tells the machine that it is dealing with a tuple 
    for i in args:
        print(i)
print(mult(1,2,3,4,5,6,7,8,9))

names = ['denis','luke','james','martin','bertin']
*beginning,middle,last = names
print(beginning)
print(middle)
print(last)