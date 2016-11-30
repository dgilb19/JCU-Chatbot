import test2


def isOdd(number):
    return number % 2 == 1


class isOddTests(test2.TestCase):
    def testOne(self):
        self.failUnless(isOdd(1))

    def testTwo(self):
        self.failIf(isOdd(2))

    # def testThree(self):
    #     self.failUnless(isOdd(4))


def main():
    test2.main()

if __name__ == '__main__':
    main()







# def func(x):
#     return x + 1
#
# def test_answer():
#     assert func(3) == 5





# def testy_mctestface(num):
#     """idk what im doing"""
#     return num * num
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
