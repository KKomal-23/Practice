#class Student:
 #   def __init__(self,name, marks_sci,marks_math,marks_marathi):
  #      self.name = name
   #     self.marks_sci = marks_sci
    #    self.marks_math = marks_math
     #   self.marks_marathi = marks_marathi

    #def __str__(self):
     #   return str(self.__dict__)
    #def __repr__(self):
     #   return str()
    
    #def avg(self):
     #   av = (self.marks_sci + self.marks_math + self.marks_marathi)/3
      #  print(av)
    
#s1 = Student("dhruv", 94,95,96)
#print(s1)
#s1.avg()
#s2 = Student("ananya", 35,78,93)
#print(s2)
#s2.avg()
        


#class office:
 #3   def __init__(self,empl_id, expe):
   #     self.employee_id = empl_id
    #    self.experience = expe
        
    #print("inside class office")

from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod          ### these are abstractmethod, we could not implement methods 
                                ## here.
    def airbags(self):
        pass
    @abstractmethod
    def wheels(self):
        pass
    @abstractmethod
    def steering(self):
        pass
    @abstractmethod
    def safety_sensors(self):
        pass
    
class tata(car):
    def engine(self):
        print("1200 cc and BS6")
    def airbags(self):
        print("8 airbags")
    def wheels(self):
        print("5 alloy wheels")
    def steering(self):
        print("power steerings")
    def safety_sensors(self): ### All these methods are colled as concrete method
                              ## all abstract methods are mandatory for all subclass.
        print("12 sensors")
    

    pass


#nexon = tata()
#nexon.engine()
#nexon.airbags()
#nexon.safety_sensors()
#nexon.wheels()

#class hyundai():
 #   pass

#class maruti_suzuki():
 #   pass

#class RBI(ABC):
 #    @abstractmethod
  #   def saving_acct(self):
   #      pass
    # @abstractmethod
     #def personal_loan(self):
      #   pass
     #@abstractmethod
     #def home_loan(self):
      #   pass
     #@abstractmethod
     #def fd():
      #   pass

#class SBI(RBI):
 #   def saving_acct(self):
  #      print("SBI provides saving accounts")
   # def personal_loan(self):
    #    print("SBI provides personal loan")
    #def home_loan(self):
     #   print("10000 home loans provided")
    #def car_loan(self):
     #   print("20000 car loans provided")
    #def fd():
     #   print("20000000 people having fds")

#obj = SBI()
#obj.car_loan()

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def debit(self,amount):
        self.balance -= amount
        print(f"Rs. {amount} debited from your account")
        print("Available Balance = ", self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print(f"Rs. {amount} credited to your account")
        print("Available Balance = ", self.get_balance())
    def get_balance(self):
        return self.balance

#Acc = Account(10000, 2344556)
#Acc.credit(1678)
#Acc.debit(1234)

class Person:
    name = "kartik"

    def change_name(self, name):
        self.name = name       ##Person.name and self.name both are different
#p = Person()
#p.change_name("Krishnaam") ## if we want chnge the class attribute use = Person.name instead
                           ## of self.name
#print(p.name)
#print(Person.name)
class AS:
    Nm = "Sakshi"
    def c_name(self, name):
        AS.Nm = name
#A = AS()
#A.c_name("Kalpana")
#print(A.Nm)
#print(AS.Nm)
### Inheritance
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started....wroom..wroom...")
    @staticmethod
    def stop():
        print("car stoped.....")
class Tata(Car):
    def engine(self,engine):
        self.engine = engine
        print(f" {self.engine} gets started")
class Nexon(Tata):
    def __init__(self, color,type):
        self.color = color
        super().__init__(type)
        print(f"Nexon is {self.color} Tata car")
#NX = Nexon("blue","electric")
#print(NX.color)
#print(NX.engine(1200))
#print(NX.start())
#print(NX.type)
#class A:
 #   def __init__(self , type):
  #      self.type = type
   #     print("A is ", self.type)
#class B(A):
 #   def __init__(self,name,type):
  #      self.name = name
   #     super().__init__(type)
    #    print(f"{self.name} is a person")
#b = B("bob","mamle")

class komal():
    print("hello")
k = komal()










 


    











    


    

   








        



