import re


class PeopleIndex:
    def __init__(self, people_str):
        self.people_str = people_str

    def __str__(self):
        return "{}".format(self.people_str)

    def people_passer(self, message_text):
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if message_text in line:
                    self.people_str = line.title().split(", ")[0]
                    """returns the appropriate name from the csv file"""

# TODO make it so that if they only put it fisrt name it still works and if there is two of the same name it gives the user an option about which one


    def change_words_to_jerry(self, message_text):
        if re.match(r'.*jerry', message_text, re.I):
            self.people_str = "this is Jerry"
        else:
            self.people_str = "I know you are asking about someone, but I don't know who that is."

