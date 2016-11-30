import unittest
from app import get_reply


class App_test(unittest.TestCase):
    def testOne(self):
        self.assertEquals(get_reply("Hello"), "Hello, how can I help you today?")

    def testTwo(self):
        self.assertEquals(get_reply("Can you show me the map?"), "Here's a map!")

    def testThree(self):
        self.assertEquals(get_reply("reverse thing"), "Reversed: gniht")

    def testFour(self):
        self.assertEquals(get_reply("random words"), "idk what you are saying")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
