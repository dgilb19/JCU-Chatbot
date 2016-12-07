import unittest
from app import get_reply


class App_test(unittest.TestCase):
    def testOne(self):
        self.assertEquals(get_reply("Hi", list_test='', last_name_used=''), "Hello, how can I help you today?")

    def testTwo(self):
        self.assertEquals(get_reply("Can you show me the map?", list_test='', last_name_used=''), "Here's a map! https://maps.jcu.edu.au/campus/townsville/")

    def testThree(self):
        self.assertEquals(get_reply("reverse thing that is awesome", list_test='', last_name_used=''), "Reversed: emosewa si taht gniht")

    def testFour(self):
        self.assertEquals(get_reply("random thingy", list_test='', last_name_used=''), "idk what you are saying")

    def testFive(self):
        self.assertEquals(get_reply("what", list_test='', last_name_used=''), "I know you are asking a question but I'm not that smart yet! :what")

    def testSix(self):
        self.assertEquals(get_reply("when", list_test='', last_name_used=''), "I know you are asking when something is, but I'm not that smart yet!")

    def testSeven(self):
        self.assertEquals(get_reply("who", list_test='', last_name_used=''), "Are you looking for Jerry?")

    def testEight(self):
        self.assertEquals(get_reply("building 34", list_test='', last_name_used=''),
                          "Are you looking for this building? \nhttps://maps.jcu.edu.au/campus/townsville/?location=34")

    def testNine(self):
        self.assertEquals(get_reply("log", list_test='', last_name_used=''), "log")

    def testTen(self):
        self.assertEquals(get_reply("last message", list_test='', last_name_used=''), "last message")

    def testEleven(self):
        self.assertEquals(get_reply("daniel", list_test='', last_name_used=''), "Daniel Gilbert")

    def testTwelve(self):
        self.assertEquals(get_reply("daniel gilbert", list_test='', last_name_used=''), "Daniel Gilbert")

    def testThirteen(self):
        self.assertEquals(get_reply("exam period", list_test='', last_name_used=''), "Exam Period")

    def testFourteen(self):
        self.assertEquals(get_reply("study", list_test='', last_name_used=''), "Study Vacation")

    def testFifteen(self):
        self.assertEquals(get_reply("week", list_test='', last_name_used=''), "O Week")

    def testSixteen(self):
        self.assertEquals(get_reply("exam", list_test='', last_name_used=''), "Exam Period")

    def testSeventeen(self):
        self.assertEquals(get_reply("when is exam week?", list_test='', last_name_used=''), "Exam Period")

    def testEighteen(self):
        self.assertEquals(get_reply("daniel gilbert", list_test='', last_name_used=''), "What about Daniel Gilbert?")

    # def testNineteen(self):
    #     self.assertEquals(get_reply("what", list_test='daniel gilbert'), "good job")

    def testNineteen(self):
        self.assertEquals(get_reply("what is his email", list_test="ted cruz", last_name_used=''), "ted.cruz@my.jcu.edu.au")

    def testNineteenPointOne(self):
        self.assertEquals(get_reply("what is his email", list_test="", last_name_used='ted cruz'), "ted.cruz@my.jcu.edu.au")

    def testTwenty(self):
        self.assertEquals(get_reply("where is Humanities", list_test="", last_name_used=''), "Are you looking for this building? \nhttps://maps.jcu.edu.au/campus/townsville/?location=3")

    def testTwentyone(self):
        self.assertEquals(get_reply("what is Daniels email", list_test="", last_name_used=''), "daniel.gilbert1@my.jcu.edu.au")

    def testTwentytwo(self):
        self.assertEquals(get_reply("when is the maths exam", list_test="", last_name_used=''), "maths 21/5")

    def testTwentythree(self):
        self.assertEquals(get_reply("maths", list_test="", last_name_used=''), "maths, 21/5")

    def testTwentyfour(self):
        self.assertEquals(get_reply("last message", list_test="TestyMcTestFace", last_name_used=''), "TestyMcTestFace")

    def testTwentyfive(self):
        self.assertEquals(get_reply("exam", list_test="", last_name_used=''), "Exam Period")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
