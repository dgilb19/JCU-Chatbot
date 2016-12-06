import re


class DateIndex:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        return "{}".format(self.date_str)

    def date_passer(self, message_text):
        with open("datelist.csv") as datelist:
            for line in datelist:
                if message_text in line:
                    self.date_str = line.title().split(", ")[0]
                    """returns the appropriate name from the csv file"""

    def exam_list_passer(self, message_text):
        with open("examlist.csv") as examlist:
            for line in examlist:
                if "maths" in examlist:
                # if line.split(", ")[0] in message_text:
                # if re.match(message_text, line):
                    self.date_str = line.title().split(", ")[0]
                else:
                    self.date_str = "this shouldnt be here"
# TODO fix this, it dont work, idk why

                    # line_name = line.split(", ")[0]
                    # line_length = len(line_name)
                    # line_first_name = line_name.split(" ")[0]
                    # line_last_name = line_name.split(" ")[1]
                    # if line_name or line_first_name or line_last_name in message_text:
                    #     line = line[:line_length].title()
                    #     self.date_str = line
                    # else:
                    #     self.date_str = "I know you are asking when something is, but I'm not that smart yet!"

# TODO work on this, add some events they can ask about questions, same as people module but probs less complex, probably
