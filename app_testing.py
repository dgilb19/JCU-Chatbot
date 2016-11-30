import unittest
from app import get_reply


# def number_add(num):
#     return num + num == 4
#
#
# class Bot_Unittest(unittest.TestCase):
#     def testOne(self):
#         self.failUnless(number_add(3))
#

class App_test(unittest.TestCase):
    def testOne(self):
        self.assertEquals(get_reply("Hello"), "Hello, how can I help you today?")

    def testTwo(self):
        self.assertEquals(get_reply("Can you show me the map?"), "Here's a map!")



def main():
    unittest.main()

if __name__ == '__main__':
    main()
