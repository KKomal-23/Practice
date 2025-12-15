import unittest
#### unit testing in python means to check small part of codes like functions 
#  class, methods are working correct or not.
# unittest is built in framework in python.

#def add(a,b):
 #   return (a+b)

#class test_add(unittest.TestCase):
#    def test_add(self):
 #       self.assertEqual(add(2,3),5)

#unittest.main()

#def sub(a,b):
 #   return (a-b)

#class test_sub(unittest.TestCase):
 #   def test_sub(self):
  #      self.assertAlmostEqual(sub(10,4),6)

#unittest.main()

#class Test_StringUpper(unittest.TestCase):
 #   def test_StringUpper(self):
  #      self.assertEqual("hello".upper(),"HELLO")
#unittest.main()

#class TestEndsWithString(unittest.TestCase):
 #   def test_StringEndsWith(self):
  #      self.assertEndsWith("Hello","o")
#unittest.main()

#class Test_ListLength(unittest.TestCase):
 #   def test_ListLength(self):
  #      self.assertEqual(len([2,3,4,5,6,7,8,9,10,1]),10)
#unittest.main()

#class Test_Member(unittest.TestCase):
 #   def test_member(self):
  #      self.assertIn(5, [2,5,8])

#unittest.main()

#class Test_Dict(unittest.TestCase):
 #   def test_dict_value(self):
  #      d = {"name": "Koumal", "age": 20}
   #     self.assertEqual(d["name"], "Koumal")

#unittest.main()

#def Division(a, b):
 #   return a / b

#class TestException(unittest.TestCase):
 #   def test_zero_division(self):
  #      with self.assertRaises(ZeroDivisionError):
   #         Division(5, 0)

#unittest.main()

USERNAME = "Admin"
PASSWORD = "Admin@123"

LOGGED_IN_SUCCESS = "Logging successfull"
ENTER_CREDENTIALS = "Enter your credentials"
INVALID_CREDDENTIALS = "Invalid credentials"


def fb_login(username = None, password = None):
    if username == USERNAME and password == PASSWORD:
        return LOGGED_IN_SUCCESS
    elif username is None or password is None:
        return ENTER_CREDENTIALS
    elif username != USERNAME or password != PASSWORD:
        return INVALID_CREDDENTIALS
    
print(fb_login("Admin", "Admin@123"))
print(fb_login("Adminnnnn","Admin@123"))

class Fb_Login_Case(unittest.TestCase):  # Test class
    def test_with_valid_credentials(self):   #test case
        result = fb_login("Admin","Admin@123")
        self.assertEqual(result,LOGGED_IN_SUCCESS)

    def test_with_no_credentials(self):
        result = fb_login()
        self.assertEqual(result,ENTER_CREDENTIALS)
    
    def test_with_invalid_username(self):
        result = fb_login("Admin43","Admin@123")
        self.assertEqual(result,INVALID_CREDDENTIALS)
    
    def test_with_invalid_password(self):
        result = fb_login("Admin","Admin@12345456")
        self.assertEqual(result,INVALID_CREDDENTIALS)

    def test_with_invalid_credentials(self):
        result = fb_login("Admin23","Admin@9887")
        self.assertEqual(result,INVALID_CREDDENTIALS)

#if __name__ == "__main__":
 #   unittest.main()          # Test runner

def fb_login(username = None, password = None):
    if username == USERNAME and password == PASSWORD:
        return LOGGED_IN_SUCCESS + "."
    elif username is None or password is None:
        return ENTER_CREDENTIALS
    elif username != USERNAME or password != PASSWORD:
        return INVALID_CREDDENTIALS
    
class Fb_Login_Case(unittest.TestCase):  # Test class
    def test_with_valid_credentials(self):   #test case
        result = fb_login("Admin","Admin@123")
        self.assertEqual(result,LOGGED_IN_SUCCESS)

    def test_with_no_credentials(self):
        result = fb_login()
        self.assertEqual(result,ENTER_CREDENTIALS)
    
    def test_with_invalid_username(self):
        result = fb_login("Adminnnn","Admin@123")
        self.assertEqual(result,INVALID_CREDDENTIALS)
    
    def test_with_invalid_password(self):
        result = fb_login("Admin","Admin@oh")
        self.assertEqual(result,INVALID_CREDDENTIALS)

    def test_with_invalid_credentials(self):
        result = fb_login("Admin23","Admin@567")
        self.assertEqual(result,INVALID_CREDDENTIALS)

if __name__ == "__main__" :
    unittest.main()
## test cases always runs in alphabetical order.hence test_with_valid_credentials
# runs in last. failure of testcase indicated by "F"
    




    


