#def funvt1():
 #   print("inside function 1")
#funvt1()

#def funct(f1):
 #   print("inside function funct1")
  #  def funct2(x,j):
   #     print("##############")
    #    f1(x,j)
     #   print("**************")
    #return funct2
#@funct
#def add(a,b):
 #   sum = a + b
  #  print(sum)
#add(20,30)

L = [1,19,30,40,50]
#c = [x for x in L if x%2==0]
#print(c)

Q = [20,44,34,345,24]
#ad = [x+5 for x in Q]
#print(ad)

class Student:
    def __init__(self,name, marks_sci,marks_math,marks_marathi):
        self.name = name
        self.marks_sci = marks_sci
        self.marks_math = marks_math
        self.marks_marathi = marks_marathi

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str()
    
    def avg(self):
        av = (self.marks_sci + self.marks_math + self.marks_marathi)/3
        print(av)
    
#s1 = Student("dhruv", 94,95,96)
#print(s1)
#s1.avg()
#s2 = Student("ananya", 35,78,93)
#print(s2)
#s2.avg()
def f1():
    print("inside f1")
    def f2():
        print("inside f2")
        def f3():
            print("inside f3")
        f3()
    f2()
#f1()
### methods of list:- append , insert,pop,remove,index,reverse,sort(),extend(),clear,count
### methods of dict:-keys(),value(),items(),update(),pop(),popitem(),setdefault(),clear()
#s= "asdfdgfgfz"
#reversed_str = ""
#for i in s:
 #   reversed_str = i + reversed_str
#print(reversed_str)
        
#text = "Python"
#reversed_str = ""

#for ch in text:
 #   reversed_str = ch + reversed_str   # add character in front
#print(reversed_str) 
#text = "Python"
#reversed_str = text[::-1]
#print(reversed_str)    
#a ="100"
#num = int(a)
#print(num,type(num))
#s = {1, 2, 3, 4}
#s.discard(3)
#print(s)
#s.discard(3)
#print(s)
#s.remove(1)
#print(s)
#student = {"name": "Raj", "age": 20}
#student["marks"] = 90
#print(student)
#student.update({"city":"mumbai","mobno":1232434})
#print(student)

class A:
    def show(self):
        print("inside A")
class B(A):
    def show(self):
        print("Inside B")
class c(B,A):
    def show(self):
        print("Inside C")
class D(c,B):
    def show(self):
        print("Inside D")
#d = D()
#d.show()
## check mro
#print(D.__mro__)
# i in range(1,6):
 #   print("*"*i)
#for i in range(1,6):
 #   print("*"*i)

for i in iter(int,1):
    print("infinite")









    
