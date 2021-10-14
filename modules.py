#date :12/9/2021
#programmer : Frank

#the random method generates floats between 0 and 1
import random as rd
print(rd.random())
a=rd.random
print(round(a,3))
#uniform generates a float between any range you give
print(rd.uniform(5,7))
#randint generates a random integer
print(rd.randint(78,90))
#randrange prints a number within any given range with or without a step
print(rd.randrange(1,7,5))#with a step which is "5"
print(rd.randrange(1,7))#without step

age=[1,32,56,45,3]
#the choice method selects an element from a list 
print(rd.choice(age))
#the choices method selects a number of elements from a list
print(rd.choices(age,k=3))
#the sample method does not take the keyword "k="
print(rd.sample(age,3))
