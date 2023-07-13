#date :19/9/2021
#programmer : Frank

class Faculty:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        # self.dean = dean

class Departments(Faculty):
        def __init__(self,name,location,head):
             self.head = head
             Faculty.__init__(self,name,location)
           

f1=Faculty('FET','campus_A')  
d1=Departments('CE','G-block','Bertin')
print(d1.location)
print(d1.name)
