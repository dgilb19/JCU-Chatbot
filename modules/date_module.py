import re


class DateIndex:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        return "{}".format(self.date_str)

    def date_passer(self, message_text):
        with open("datelist.csv") as datelist:
            for line in datelist:
                line_name = line.split(", ")[0]
                line_length = len(line_name)
                if line_name in message_text:
                    line = line[:line_length].title()
                    self.date_str = line



        self.date_str = "I know you are asking when something is, but I'm not that smart yet!"

#TODO start/finish this, add some events they can ask about same as people module but probs less complex
