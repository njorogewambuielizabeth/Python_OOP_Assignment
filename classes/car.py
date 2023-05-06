# 2) Create 3 files in the classes directory car.py, fruit.py, 
# and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

class Car:
    make="BMW"
    def __init__(self,model,color,mileage):
        self.model=model
        self.color=color
        self.mileage=mileage
    def start(self):
        print(f"{self.model} is my favourite")
        
    def drive(self):
        print(f"My BMW is {self.color} in color")  
             
    def stop(self):
        print(f"My vehicle's speed is {self.mileage} mph")
        
car1=Car("BMW M3","white",155) 
car1=Car("BMW X7","Purple",180) 