class Things2:
    def __init__(self, sentence):
        self.sentence = sentence

    def __str__(self):
        return "{}".format(self.sentence)

    def new_string(self):
        self.sentence = "this is a new sentence"

    def new_string_two(self):
        self.sentence = "this is a new string also"
