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

    def exam_list_passer(self, message_text):
        with open("examlist.csv") as examlist:
            for line in examlist:
                if message_text in line:
                    # line = line.split(", ")
                    # self.date_str = "{}, {}".format(line[0], line[1])
                    self.date_str = line

    def next_class_passer(self):
        self.date_str = 'I dont have enough time to finish this, but lets just pretend that it works, ok?'

# ******** leave this here
    # def exam_passer(self, message_text):
    #     with open("examlist.csv") as examlist:
    #         for line in examlist:
    #             if line.split(", ")[0] in message_text:
    #                 self.date_str = "the {} exam is on the {}".format(line.split(", ")[0], str(line.split(', ')[1]))
    #         else:
    #             self.date_str = "this aint workin"
# ******




