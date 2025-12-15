#t =  [(1,3), (5,1), (5, 8),(6, 0), (2, 6)]
#sort_t = list(sorted(t, key=lambda x:x[1])) 
#print(sort_t)






#2
#l =[2,34,5,6,6]
#rl = map(l,lambda x: x%2==0)
#print(rl)




## Q4.
#for i in iter(int,1):
 #   print("infinte loop")


#class Car:
 #   def __init__(self,type):
  #      self.type = type
   #     print("type of car is", self.type)
        
#class Tata(Car):
 #   def __init__(self, color,type):
  #      self.color = color
   #     super().__init__(type)
    #    print("color of the car is ", self.color)
#nx = Tata("black","electric")
#print(nx)

from abc import ABC , abstractmethod
class RBI:
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def account(self):
        pass
class SBI(RBI):
    def loan(self):
        print("loan can be given on 5% interest")
    
    def account(self):
        print("Accounts created")

#sb = SBI()
#sb.loan()

class Student:
    def __init__(self,name,password):
        self.name = name
        self.__password = password

    def avg(self):
        

St = Student("Sakshi",2343445)
St._Student__.password   
    



















