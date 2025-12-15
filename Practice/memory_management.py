import dis
import sys

# def sample():
#     return 10+20

# dis.dis(sample)

a = []
print(sys.getrefcount(a)) # reference count of a is 2

b = a
print(sys.getrefcount(a)) # reference count of b is 3

