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
        self.assertEquals(get_reply("random thingy"), "idk what you are saying")

    def testFive(self):
        self.assertEquals(get_reply("what"), "I know you are asking a question but I'm not that smart yet! :what")

    def testSix(self):
        self.assertEquals(get_reply("when"), "I know you are asking when something is, but I'm not that smart yet!")

    def testSeven(self):
        self.assertEquals(get_reply("who"), "I know you are asking about someone, but I'm not that smart yet!")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
