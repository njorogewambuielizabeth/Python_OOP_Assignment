class Student:
    school="AkiraChix"
    def __init__(self,name,age,nationality):#is a constructor
        self.name=name
        self.age=age
        self.nationality=nationality
    def greet_student(self):
        return f"Hello {self.name}, welcome to {self.school}" 
    def year_of_birth(self):
        year=2023 - self.age
        return f"Hello {self.name}, you were born in {year}" 
    def show_full_name(self):
        return f"Hello {self.name}"  
    def show_initials(self):
        name_parts=self.name.split(" ")
        initials=[name[0].upper() for name in name_parts]
        return ".".join(initials) 
    
    
       