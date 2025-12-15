#def funct(fn):
#    print("inside function 1")
 #   def funct2(v,n):
  #      print("inside function 2")
   #     fn(v,n)
    #    print("calling decorator")
    #return funct2
#@funct
#def add(a,b):
 #   sum = a+b
  #  print("addition of a , b is :",sum)
#print(add)
#add(23,45)

#def funct(f1):
 #   print("inside function funct1")
  #  def funct2(x,j):
   #     print("##############")
    #    f1(x,j)
     #   print("**************")
    #return funct2
#@funct
#def sub(a,b):
 #   sub = a - b
  #  print(sub)
#sub(30,20)

## Time decorator
import time
#def time_execution(f):
 #   def wrapper():
  #      t1 = time.time()
   #     f()
    #    t2 = time.time()
     #   print(f"time taken by {__name__} is {t2-t1}")
    #return wrapper
#@time_execution
#def sleep_time1():
 #   time.sleep(4)
#sleep_time1()

#t1 = time.time() python takes time from epoch time. sleep.time(4) this command stops program
#print(t1)         for 4.sec and then execute
#time.sleep(4)
#t2 = time.time()
#print(t2)
#print(t2-t1)
#def funct1(f):
 #   def inner():
  #      t1= time.time()
   #     f()
    #    t2 = time.time()
     #   print("Total sleeping time is ",t2-t1)
    #return inner

#@funct1
#def stop_time():
 #   time.sleep(7)
#stop_time()
############################################
##authenticator
#Credentials = {"kavya":"kavya@123","akay":"akay@123","Sid":"Sid@3454"}
#def authenticate(f):
 #   def wrapper(un,pw):
  #      if Credentials.get(un) == pw :
   #         f(un,pw)
    #    else:
     #       print("Invalid credentials")
    #return wrapper
#@authenticate
#def login(username,password):
 #   print("Login Successfully!!!!!")
#login("akay","akay@123")
#login("komal","komal@123")
########################################################### 
# 
# DECORATORS
#import time
#t1 = time.time()
#print(t1)
#time.sleep(5)


#def time_execution(f):
 #   def wraper():
  #      t1 = time.time()
   #     print(t1)
    #    f()
     #   t2 = time.time()
      #  print(t2)
       # print("total sleeping time is",t2-t1) 
    #return wraper

#@time_execution
#def sleeptime():
 #   time.sleep(5)


#def greet(fn):  ##fn = add
    #def funct1(x,y):   ## add = funct1
    #    print("Good evening")
   #     fn(x,y)
  #      print("hello thank you for using this function")
 #   return funct1

#@greet
#def add(a,b):
 #   print(a+b)
#add(10,20)

def time_execution(fx):
    def funct2():
        t1 = time.time()
        fx()
        t2 = time.time()
        print("required time :", t2-t1)
    return funct2


@time_execution
def sleep_time():
    time.sleep(4)
sleep_time()




