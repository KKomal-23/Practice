##### EXCEPTION HANDLLING
### There are two types of exceptions:
# 1. Predefined Exception
# 2. User defined Exception(Custom Exception).

# 1. PREDEFINED EXCEPTION (In built exception)
# exception which automatically raised by python machine.

#try:
 #   res = 10/0
#except ZeroDivisionError:
 #   print("denominator should not zero") 

#try:
    #l = [1,3,5,6,6][10]
 #   x = int(input("enter a number :  "))
  #  y = int(input("Enter a number:  "))
   # print(x/y)
      #  risky code

#except ZeroDivisionError:
 #   print("denominator must not be zero")
#except ValueError:
 #   print("please enter a number")
#except:
 #   print(ex)
    
#else:
 #   pass
#finally:
 #   print("Inside finally")


#try:
 #   print("Inside try 1")
  #  try:
   #     L =[23,43,45,435,234][12]
        #a = int("adsfd")
    #except TypeError:
     #   print("please enter credentials properly")
    #except IndexError:
     #   print("inappropriate index")
    ##   print("finally of try 2")
#except:
 #   print("exception handeled by try1 ")
#finally:
 #   print("finally of try 2 also executed")

#try:
    #D = {"Name": "rahul","Age":"21","City":"Mumbai"}
    #print(D["mob_no"]) ## key error
 #   A = "adsfdf"+ 37   ## Type error
#except KeyError:
 #   print("Please enter valid info")
#except TypeError as msg:
 #   print("Error :-", msg)
#else:
 #   print(D["mob_no"])
    #print(A)
#finally:
 #   print("Progrram Executed")

## Attribute error
#try:
 #   A = 35
  #  A.append()   ## Attribute Errror
#except AttributeError as e:
 #   print("Error : ",e)
### File not found error
#try :
 #   file = open("interview_question.txt","r")
#except FileNotFoundError as ex :
 #   print("FileNotExist", ex)
#else:
 #   data = file.read()
  #  print(data)
#finally:
 #   file.close()

#try:
 #   import Modulenotexist
#except ModuleNotFoundError:
 #   print("Module not found, Please install the module")
#finally:
 #   print("Execution done")

#######################################################
## pyi file :- Interface file.
#class Custom_Exception(Exception): ## parrent is exception.
 #   pass

#raise  Custom_Exception("Insufficient Fund") 
## Custom Exception means user define exception.we can give message also in paranthesis
## to call exception use "raise" keyword.
#class CustomException(Exception):
 #   def __init__(self, msg):
        #print("Inside INIT ")
        #self.msg = msg

#raise CustomException("Insufficient Fund!!!!")

#class SalaryNotInRange(Exception):
 #   def __init__(self, msg):
  #      self.msg = msg

#sal = 25000
#try:
 #   if sal < 35000: ## risky code aahe so try and except use kele.
  #     raise SalaryNotInRange("Salary is not in range") 
#except SalaryNotInRange as msg:
 #   print(msg)

#for i in range (1,15,2):
 #   print(i)
#############################################################
#class CustomError(Exception):
 #   def __init__(self,messege):
  #      super().__init__(messege) ## to call parent class (exception class cha) constructor.
   #     self.messege = messege
#def Check_value(value):
 #   if value < 0:
  #      raise CustomError("Given value can not be negative")
#try:
 #   num = int(input("Enter the value :- "))
  #  Check_value(num)
   # print("Square of given value is :", num*num)
#except CustomError as ex:
 #   print("Custom Error Occured :", ex.messege)
#except ValueError:
 #   print("Please enetr the valid integer")
#########################################################
#USERNAME = "Kartik"
#PASSWORD = "Kartik@123"

#class AuthenticationError(Exception):
 #   def __init__(self):
  #      super().__init__("Authentication failed")
    

#User_Username_input = input("Enter Username :- ")
#User_Username_password = input("Enter Password :- ")
#try:
 #   if User_Username_input != USERNAME and User_Username_password != PASSWORD:
  #      raise AuthenticationError()
   # else:
    #    print("Authentication successfull!!!!")
#except AuthenticationError as e:
 #   print(e.args[0])
###############################################################################
## INVALID EMAIL ID
#class InvalidEmailId(Exception):
 #   def __init__(self):
  #      super().__init__("Invalid Email Address")

#try:
 #   email = "koumaljadhav.com"
  #  if "@" not in email:
   #     raise InvalidEmailId()
#except InvalidEmailId as e:
 #   print("Error :",e)

#class InvalidEmailId(Exception):
 #   def __init__(self):
  #      super().__init__("Invalid Email Format")

#em = input("Enter email id :- ")
#try:
 #   if "@" not in em:
  #      raise InvalidEmailId()
   # else:
    #    print("Email Login successfull!!")
#except InvalidEmailId as e:
 #   print("Error :-",e)
#finally:
 #   print("In finally")
######## Unauthorized access
#class UnauthorisedAccess(Exception):
 #   pass
#try:
 #   user_role = input("Enter user role :- ")
  #  if user_role != "admin":
   #     raise UnauthorisedAccess("Only admin can access")
#except UnauthorisedAccess as e:
 #   print("Error : ", e)
#else:
 #   print("Access Authorised")
#finally:
 #   print("program executed")

class InvalidAgeError(Exception):
    def __init__(self):
        super().__init__("Age must be greater than 18")


def validate_age(age):
    if age < 18 or age >120:
        raise InvalidAgeError()
try:
    age = int(input("Enter the age :-"))
    validate_age(age)
    print("Given Age is : ", age)
except InvalidAgeError as e:
    print("Given age is out of range :",e)
except ValueError as ex:
    print("Error :", ex)
else:
    print("You are eligible to vote")
finally:
    print("execution done!!!!!!!!")

    











    