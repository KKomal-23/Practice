print("hellooooo")
#### Conditional statement###
## if-elif-else is syntax.
# if (condition):  condition can be anything e.g. age>=18 , boolean (True,False)
#     statement                 if condition is true then only stat will execute.
# syntax :- if:
#            statement
#           elif:
#            statement
#           else:
#            statement  

# examples:
num = -5
if num > 0:
    print("Number is positive")

#age = 18
#if age >= 18:
 #   print("You are eligible to vote")

age = 16
if age >= 18:
    print("You can vote")
else:
    print("You are not eligible to vote")

#num = 7
#if num % 2 == 0:
 #   print("Even number")
#else:
 #   print("Odd number")

marks = 75

if marks >= 90:
   print("Grade: A")
elif marks >= 75:
   print("Grade: B")
elif marks >= 50:
   print("Grade: C")
else:
   print("Grade: Fail")

#num = 0

#if num > 0:
 #   print("Positive number")
#elif num < 0:
 #   print("Negative number")
#else:
 #   print("Zero")

#a = 10
#b = 15
#if true:
 #  print("10")

## for loop 

#for i in range(10,1,-1):
 #  print(i)
#L = [1,19,30,40,50]
#c = [x for x in L if x%2==0]
#print(c)

#Q = [20,44,34,345,24]
#ad = [x+5 for x in Q]
#print(ad)