import unittest
from app import get_reply


class App_test(unittest.TestCase):
    def testOne(self):
        self.assertEquals(get_reply("Hello"), "hello, how can I help you today?")

    def testTwo(self):
        self.assertEquals(get_reply("Can you show me the map?"), "Here's a map! https://maps.jcu.edu.au/campus/townsville/")

    def testThree(self):
        self.assertEquals(get_reply("reverse thing"), "Reversed: gniht")

    def testFour(self):
        self.assertEquals(get_reply("random thingy"), "idk what you are saying")

    def testFive(self):
        self.assertEquals(get_reply("what"), "I know you are asking a question but I'm not that smart yet! :what")

    def testSix(self):
        self.assertEquals(get_reply("when"), "I know you are asking when something is, but I'm not that smart yet!")

    def testSeven(self):
        self.assertEquals(get_reply("who"), "Are you looking for Jerry?")

    def testEight(self):
        self.assertEquals(get_reply("building 34"),
                          "Are you looking for this building? \nhttps://maps.jcu.edu.au/campus/townsville/?location=34")

    # def testNine(self):
    #     self.assertEquals(get_reply("log"), "log")
    #
    # def testTen(self):
    #     self.assertEquals(get_reply("last message"), "last message")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
