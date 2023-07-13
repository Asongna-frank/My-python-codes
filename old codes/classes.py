#date :19/9/2021
#programmer : Frank

class Student:
    def __init__(self,name,matricule):
        self.name = name
        self.matricule = matricule
    def codes_written(self):
        print('you are inside the function')

class Shop:
    def __init__(self):
        pass

class Pant:

        def __init__(self,price,color,size):
            self.price = price
            self.color = color
            self.size = size

        def change_prize(self,new_price):
            self.price = new_price
            return self.price

        def discount(self,percentage):
            dis = (percentage/100)*self.price
            reduced_price=self.price - dis
            return (self.change_prize(reduced_price))

class Sales_person:
    def __init__(self,identifier,phone_number):
        pass
    def items_sold():

test=Pant(1000,"red",3)
print(test.discount(10))


            




    