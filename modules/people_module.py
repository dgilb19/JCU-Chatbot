import re


class PeopleIndex:
    def __init__(self, people_str):
        self.people_str = people_str

    def __str__(self):
        return "{}".format(self.people_str)

    def change_words_to_jerry(self, message_text):
        if re.match(r'.*jerry', message_text, re.I):
            self.people_str = "this is Jerry"
        else:
            self.people_str = "I know you are asking about someone, but I'm not that smart yet!"
