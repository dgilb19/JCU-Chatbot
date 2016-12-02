
class PeopleIndex:
    def __init__(self, people_str):
        self.people_str = people_str

    def __str__(self):
        return "{}".format(self.people_str)

    def change_words_to_jerry(self):
        self.people_str = "Are you looking for Jerry?"

    def make_words_new(self):
        self.people_str = "these are the newest words"
