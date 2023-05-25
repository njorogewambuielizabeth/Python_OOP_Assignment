class Fruit:
    fruit_type = "Edible"

    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor
        
    def eat(self):
        print(f"I love {self.name}")  
        
    def wash(self):
        print(f"Berries are {self.color} in color")  
        
    def eat(self):
        print(f"Pineapples have a  {self.flavor} flavor")  
        
fruit1=Fruit("Grapes","purple","sweet")
fruit1.wash()
        
              