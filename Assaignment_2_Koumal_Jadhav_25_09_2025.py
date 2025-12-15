#print("hellooo")
#### INHERITANCE EXAMPLES ####
## SINGLE INHERITANCE
#class flowers:
 #   print("inside flower class")
  #  def colour(self):
   #     print("flowers have beautiful colours")
#class Rose(flowers):
 #   def red(self):
  #      print("Roses are red in colour")

#rose = Rose()
#rose.colour()
#rose.red()

#class shapes():
 #   def Perimeter(self):
  #      print("different geometrical figures have different perimeter")
#class square(shapes):
 #   def perimeter(self,a):
  #      pm = 4*a
   #     print("perimeter of square is:- ",pm)
#s = square()
#s.perimeter(5)
#s.Perimeter()

## MULTIPLE INHERITANCE ##
#class person():
 #   def qualities(self):
  #      print("A person must have good qualities")

#class teacher():
 #   def teach(self):
  #      print("teacher teaches all subjects")

#class student(person,teacher):
 #   def student(self):
  #      print("student studies hard")
#s  = student()
#s.teach()
#s.qualities()

#class bird:
 #   def fly(self):
  #      print("birds can fly")
#class swim:
 #   def sw(self):
  #      print("birds can swim")
#class duck(bird,swim):
 #   def quak_quak(self):
  #      print("ducks do quak quak")

#d = duck()
#d.quak_quak()
#d.sw()
#d.fly()

## MULTILEVEL INHERITANCE

#class livingBing:
 #   def breath(self):
  #      print("breathing")
    
#class humanBeing(livingBing):
 #   def walking(self):
  #      print("children and adults can walk")
   # def talking(self):
    #    print("humans can talk in various languages")
#class baby(humanBeing):
 #   def crawling(self):
  #      print("babies can do crawling")
#bab = baby()
#bab.crawling()
#bab.talking()
#bab.breath()

#class University:
 #   def university_name(self):
  #      print("university name is Mumbai university")
#class Department(University):
 #   def department_name(self):
  #      print("department is Computer science")

#class Student(Department):
 #   def student_name(self,name,id):
  #      self.name = name
   #     self.id = id
    #    print("student name is",self.name)
     #   print("student id is",self.id)
    

#my_student = Student()
#my_student.student_name("apoorva",2345)
#my_student.department_name()
#my_student.university_name()

## Hierarchical inheritance 
#class person:
 #   def __init__(self,name):
  #      self.name = name
#class HR(person):
 #   def recruitment(self):
  #      print(f"{self.name} is recruiting employee")
#class manage(person):
 #   def manager(self):
  #      print(f"{self.name} is managing the work")
#class staff(person):
 #   def employee(self):
  #      print(f"{self.name} performing his task")

#st = staff("priya")
#st.employee()
#mn = manage("aarav")
#mn.manager()

#class books:
 #   def __init__(self,name,no_pages):
  #      self.name = name
   #     self.no_pages = no_pages
    #def open(self):
     #   print(f"{self.name} book is open")
    #def close(self):
     #   print(f"{self.name} book is closed")
#class fiction(books):
 #   def type(self):
  #      print(f"{self.name} is a fiction book")
#class autobiography(books):
 #   def read(self):
  #      print(f"{self.name} reading autobiography")

#at = autobiography("wings of fire",400)  
#at.open()
#at.read()
#at.close()    

## hybrid inheritance
#class System:
 # def process(self):
  #  self.process
   # print("processing a data")
    #return "data is processed"
#class Database(System):
 # def store(self):
  #  self.store
   # print ("Storing data")
    #return "database use to store data"

#class API(System):
 # def request(self):
  #  self.request
   # print("Handling request")
    #return "handles request"

#class App(Database, API):
 # def describe(self):
  #  return f"{self.process()},\n {self.store()},\n {self.request()}"

#app = App()
#print(app.describe())

#class Bank:
 #   def info(self):
  #      print("Bank provide us various services")

#class Account(Bank):
 #   def account_details(self):
  #      print("bank account details")

#class OnlineServices(Bank):
 #   def login(self):
  #      print("User logged into online services of bank")

#class SavingsAccount(Account):
 #   def interest(self):
  #      print("Savings account gives 5% interest")

#class Onlinefeature(SavingsAccount, OnlineServices):  
 #   def online_features(self):
  #      print("We can transfer money online")

#customer = Onlinefeature()
#customer.info()
#customer.account_details()
#customer.interest()
#customer.login()
#customer.online_features()

## ABSTRACTION 

#from abc import ABC, abstractmethod

#class bank(ABC):
 #   def __init__(self,bk_name):
  #      self.bank_name = bk_name
   #     print(f"Welcome to {self.bank_name}")

#class bank_account(bank):
 #   @abstractmethod
  #  def deposit(self):
   #     pass
    #@abstractmethod
    #def withdraw(self):
     #   pass
#class saving_account(bank):
 #   def __init__(self, bk_name,balance=0):
  #      self.balance = balance
   #     super().__init__(bk_name)

    #def deposit(self,amt):
     #   self.balance += amt
      #  print(f"INR {amt} amount is deposited,avail. balance is: INR {self.balance}")
    #def withdraw(self,amt):
     #   if amt<= self.balance:
      #      self.balance -= amt
       #     print(f"INR {amt} amount withdraw,avail.balance is: INR {self.balance}")
        #else:
         #   print("Insufficient balance")
#acct = saving_account("Canara_bank",1000)
#acct.deposit(300)
#acct.withdraw(400)

#class Employee(ABC):
 #   @abstractmethod
  #  def skills(self):
   #     pass
    #@abstractmethod
    #def cal_salary(self):
     #   pass
    #def Intern(self):
     #   print("interns are most welcome")

#class full_time_employee(Employee):
 #   def __init__(self, skill , month_s):
  #      self.Skills = skill
   #     self.monthly_salary = month_s
      
    #def skills(self):
     #   return(f"{self.Skills} employee")
    #def cal_salary(self):
     #   return self.monthly_salary
#class freelancer(Employee):
 #   def __init__(self,skill,hr,rt):
  #      self.hour = hr
   #     self.rate = rt
    #    self.Skills = skill
    #def skills(self):
     #   return(f"{self.Skills} is skill of employee")
    #def cal_salary(self):
     #   return self.hour*self.rate

#emp = freelancer("code_Translator",150,500)
#print(emp.skills())
#print("salary of freelancer is", emp.cal_salary())
#ep = full_time_employee("developer",50000)
#print(ep.skills())
#print("salary of full time employee is",ep.cal_salary())


#### Decorators ####
#### Logging decorator
#def log_function(func):
 #   def funct1(*args):
  #      print("Function is about to run")
   #     res = func(*args)
    #    print("Function finished")
     #   return res
    #return funct1

#@log_function
#def hello(name):
 #   print(f"Hello {name}")

#hello("Koumal")

#### Execution time decorator
#import time

#def timing(func):
 #   def funct2():
  #      print("start timing")
   #     start = time.time()
    #    func()
     #   end = time.time()
      #  print("Time taken:", end - start)
       # print("End timing")
    #return funct2

#@timing
#def waiting_timing():
 #   time.sleep(5)
    
#waiting_timing()

#### authentication decorator

#def authentication(func):
 #   def funct3(user):
  #      if user["logged_in"]:
   #         func(user)
    #    else:
     #       print("Please log in first!")
    #return funct3

#@authentication
#def user_profile(user):
 #   print("User_name", user["name"])

#user_profile({"name": "Koumal", "logged_in": False})
#user_profile({"name": "Ananya", "logged_in": True})

#### Access control decorator
#def Access_control(func):
 #   def funct4(role):
  #      if role == "admin":
   #         func(role)
    #    else:
     #       print("Access denied")
    #return funct4

#@Access_control
#def del_file(role):
 #   print("File deleted by", role)

#del_file("admin")
#del_file("user")

#### Validation Decorator
#def Positive_no(func):
 #   def funct5(X):
  #      if X < 0:
   #         print("Please enter positive number")
    #    else:
     #       func(X)
    #return funct5
        
#@Positive_no
#def cube(X):
 #   cub = X**3
  #  print(f"cube of {X} is {cub}")


#cube(35)
#cube(-4)

##### Type checking decorator
#def checking_string(func):
 #   def funct6(word):
  #      if not isinstance(word, str):
   #         print("Argument must be a string")
    #        return
     #   return func(word)
    #return funct6

#@checking_string
#def text(word):
 #   return word.upper()

#print(text("Python"))  
#print(text([2,3,4]))      



        


  

        
     
    






        
        



    

        




     
    
    