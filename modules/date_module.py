
class DateIndex:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        return "{}".format(self.date_str)

    def date_passer(self, message_text):
        self.date_str = "I know you are asking when something is, but I'm not that smart yet!"
