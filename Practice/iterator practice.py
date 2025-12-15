#An iterator is an object that allows you to loop 
#through (iterate over) elements of a collection one at a time.
#In Python, an object is called an iterator if it has:

#__iter__() → returns the iterator object itself

#__next__() → returns the next item in the sequence
#(and raises StopIteration when no items are left)

my_list = [10, 20, 30]
iterator = iter(my_list)   # Create an iterator

#print(next(iterator))  # Output: 10
#print(next(iterator))  # Output: 20
#print(next(iterator))  # Output: 30
#print(next(iterator)) #now would raise StopIteration


class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        value = self.num
        self.num -= 1
        return value

#cd = CountDown(5)

#for num in cd:
   # print(num)


class OddNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        print("in iter method")
        return self
        pass

    def __next__(self):
         # print("in next method")
        if self.start <= self.end: # 11 <= 9
            tmp = self.start # 3
            self.start += 2 # 5
            return tmp  # 3
        else:
            raise StopIteration
        
        


#obj = OddNumbers(1,9)
#iter_object = iter(obj)
#print(next(iter_object))  
#print(next(iter_object))  
#print(next(iter_object))  
# print(next(iter_object))  
# print(next(iter_object))  
# print(next(iter_object))  


class InfiniteIterator:
    def __init__(self, st):
        self.start = st

    def __iter__(self):
        return self

    def __next__(self): 
        tmp = self.start
        self.start += 1
        return tmp
        
obj = InfiniteIterator(1)
iter_obj = iter(obj)
# for i in iter_obj:
#     print(i)

#print(next(iter_obj))
#print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))


#A generator in Python is a special type of function that produces
#values one at a time instead of returning them all at once.
#It is memory-efficient and uses the keyword yield instead of return.

#A generator is:

#A function with the keyword yield

#It returns an iterator

#It produces values lazily (only when needed)

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

def count_up_to(n):
   i = 1
   while i <= n:
      yield i
      i += 1

for num in count_up_to(5):
    print(num)


