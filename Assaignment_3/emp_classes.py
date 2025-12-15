from datetime import datetime

class Employee:
    def __init__(self, name , salary, address, email, dob):
        self.name = name 
        self.surname = self.split_name(name)
        self.salary = salary
        self.address = address
        self.email = email
        self.dob = dob
        self.age = self.calculate_age()

    def split_name(self,full_name):
        parts = full_name.split(" ",1)
        if len(parts)==2:
            return parts[0] , parts[1]
        else:
            return parts[0]
        
    def calculate_age(self):
        birth_year = int(str(self.dob)[:4])
        current_year = datetime.now().year
        return current_year - birth_year

    def __str__(self):
        return f"\n{self.__dict__}"
    
    def __repr__(self):
        return str(self)
    
