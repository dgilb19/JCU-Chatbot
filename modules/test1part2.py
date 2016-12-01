class Thing:
    def __init__(self, number=0):
        self.number = number

    def __str__(self):
        return "this is the answer: {}".format(self.number)

    def add_num(self, amount):
        self.number += amount

    def multiply_num(self, amount):
        self.number *= amount
