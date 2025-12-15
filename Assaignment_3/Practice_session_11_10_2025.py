#a = 13    ###allowed
#_ab = 25  ### allowed
#34abk = 12  ### not allowed
#@km = 34    ### not allowed
#mn_2h = 68  ## allowed
#print = 23 ## not allowed
#dir = 12   ## not allowed

## string data type method
##1. upper() , lower(), capitalize(),title(),strip(),replace(),join()
#s = "python language"
#s.upper()
#print(s.upper())
#print(s.capitalize()) ## first letter capital
#print(s.title())
#print(s.strip())
#print(s.replace("python","english"))
#print(s.swapcase())
#print(s.lstrip())
#print(s.rstrip())

## list
#lst = [3,4,5,6,5,234]
#print(lst)
#lst.append("cherry")
#print(lst)
#lst.append(8)
#print(lst)
#lst.append([45,78])
#print(lst)
#lst.append({"name":"koumal","city":"kalyan"})

#lst.append({11,12,34})
#lst.append((55,66))
#lst.append(31+8j)
#print(lst)
#lst.append("true")
#print(lst)

#lst.pop()
#lst.pop(7)

#lst.pop(11)
#print(lst)
#lst.pop(10)
#print(lst)
#lst.extend("python")
#print(lst)
#lst.extend([22,33,44,55])
#print(lst)
#lst.extend({"name":"koumal","city":"kalyan"})
#print(lst)
#lst.extend((8,9,78))
#print(lst)
#lst.extend({23,44,55})
#print(lst)
#lst.remove(6)
#print(lst)
#lst.remove(8)
#print(lst)
#lst.remove([45,78])
#print(lst)
#lst.sort()
#print(lst)
#lst.reverse()
#print(lst)
#print(lst.count("asd"))

#print(lst.index(5))
#print(lst.count(5))
#lst.pop()
#lst.pop(5)
#print(lst)
#print(lst)
#lst.sort()
#print(lst)
#lst.sort(reverse= True)
#print(lst)
#print(max(lst))
#print(min(lst))
#print(sum(lst))
#print(len(lst))
#b = lst.copy() # b is shallow copy of a but memory location for both is different.
#print(b)
#b.append(10)
#print(b)
#b.clear()
#print(b)
#del lst[1]
#print(lst)

#l1 = [2,3,45,565,556,7,8,9]
#l2 = l1            ## same memory location
#l3 = l2            ## same memory location
#l1[0] = 1
#print(l1)
#print(l2)
#print(l3)

#import copy
#l2 = copy.deepcopy(l1)
#print(l2) 
#print(id(l1[3]),id(l2[3]))   ## same id





## DICTIONARY METHOD
#d = {"name":"Kriti","Age":20}
#print(d)
#print(d.get("name"))
#print(d.get("Age"))
#print(d.get("marks",0))  ## default value
#print(d.get("city","mum"))
#print(d.get("mob_no",236276324))
#print(d.keys())
#print(d.values())
#print(d.items())  ## returns key value pair in list foramt.
#d.update({"City":"Mumbai","Dob":"04-03-2005"})
#print(d) 
#d.update({"mob_no":35435454})
#print(d)
#d.pop("Dob")
#print(d)
#d.popitem() ## removes last item
#print(d)
#d.popitem()
#d.setdefault("marks",89)
#print(d)
#d.setdefault("Pin",421003)
#print(d)

#print(d["name"])
#print(d["Age"])
# print(d[marks])   ## we can not access setdefault keys here.
#d["Pin"] = 421003
#print(d)
#d["City"] = "Mumbai"
#d["course"] = "Python"
#print(d)
#d["list"] = [2,3,4,5]
#print(d)
#d["dict"] = {"skill":"cooking"}
#d["tup"] = (2,3,4,5)
#d["set"] = {3,4,5,6}
#print(d)


## SET METHODS
#s = {2,3,4,5,6,9,11}
#s.add(1)
#s.add(7)
#s.add(8)
#s.add(10)
#print(s)

#s.discard(2)
#print(s)
#s.discard(5)
#.discard(6)
#s.discard(11)
#s.discard(34) ## if number does not exist in set then alsodiscard will not give error. 
#print(s)

#s.remove(1)
#print(s)
#s.remove(11) ## if no. does not exist then "remove" method will give key error. 
#print(s)

#s.pop()
#print(s)
#s.pop()
#print(s)
#s.clear()
#print(s)
#s.add(1)
#print(s)
#s.add("asd")  # we can add string
#print(s)
#s.add((2,3,4)) # can add tuple
#print(s)
#s.add({4,5,6,7}) # gives error "unhashable set"
#print(s)
#s.add([1,2,3]) # give error  type error"unhashable type : list"
#print(s)
#s.add({"name":"kriti"}) # same give type error
## we can not add mutable data types in set. it allows only immutable data types.

## conditional statements
#a = 1
#if a<20:
 #   print(a)
#if a>5:
 #   print("Hello")
#else:
 #   print("Hii")

a = 10
if a<12:
    a + 2
if a>5:
    a + 26
    print(a)





