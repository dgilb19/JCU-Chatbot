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
                    print "test message text is {}".format(message_text)
                    print "test line thing{}".format(line)
                    self.date_str = line.title().split(", ")[0]
                    """broken, same problem returns the appropriate name from the csv file"""

    """passes the relative exam information back"""
    def exam_list_passer(self, message_text):
        with open("examlist.csv") as examlist:
            for line in examlist:
                if message_text in line:
                    # line = line.split(", ")
                    # self.date_str = "{}, {}".format(line[0], line[1])
                    self.date_str = line

    def next_class_passer(self):
        self.date_passer = 'I dont have enough time to finish this, but lets just pretend that it works, ok?'

    def exam_passer(self, message_text):
        with open("examlist.csv") as examlist:
            for line in examlist:
                if message_text in line.split(", ")[0]:
                    # self.date_str = "the {} exam is on the {}".format(line.split(", ")[0], str(line.split(', ')[1]))
                    self.date_str = "teagnjraeignreiawgnreignriw"
            else:
                self.date_str = "this aint workin"



# TODO fix this, it dont work, idk why THIS IS LITERALLY KILLING ME

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
