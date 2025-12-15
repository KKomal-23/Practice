#print("hello python")
#def cal_sum(a,b):
 #   sum = a+b
  #  print(sum)
    #return(sum)
#cal_sum(10,20)

#def cal_sum(a,b):
  #  return a+b

#sum = cal_sum(10,20)
#print(sum)

#def print_hello():
    #print("hello world",5)

#output = print_hello()
#print(output)

def average(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return("average of a,b,c is :", avg)
#average(2,3,4)
#average(89,56,87)

#def average(*args):
 #   sum = 0
 #   for i in args:
  #      sum+=i
   # return sum/len(args)
#obj = average(457,34,3454,132,324,434,23)
#print(obj)
    
## NESTED FUNCTIONS

#def funct_1():
 #   print("inside function 1")
  #  def funct_2():
   #     print("inside function 2")
    #def funct_3():
     #   print("Inside function 3")
    #def funct_4():
     #   print("Inside function 4")
    #funct_2()
    #unct_3()
    #funct_4()

#funct_1()

#def kp():
 #   print("hello kp")
  #  def km():
   #     print("hello km")
    #    return "abc"
    #return km()            ## km memory location
#kop = kp()                 ## function kp will return memory location of 
                           ## function km this is called as 
                           ## "closure". if return function is not written for function then it will 
                           ##  gives "None" value in return.
#print(kop) 

#L = [2,3,4,5,6,7,8,9,4,5,4,5,4]
#print(L[1])
#print(L[1:6])
#for i in L:
 #   print(L[i])
#def cout():
    
 #   for i in L:
  #      rept_no = L.count(i)
   #     i+=1
   # return("repeated occurance of no.",rept_no)

#count_no = cout()
#print(count_no)

def funct(fn):
    print("inside function 1")
    def funct2(v,n):
        print("inside function 2")
        fn(v,n)
        print("calling decorator")
    return funct2



@funct
def add(a,b):
    sum = a+b
    print("addition of a , b is :",sum)
print(add)
add(23,45)






