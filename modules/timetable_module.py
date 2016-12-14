import re


class TimetableIndex:
    def __init__(self, timetable_str):
        self.timetable_str = timetable_str

    def __str__(self):
        return "{}".format(self.timetable_str)

    def timetable_passer(self, message_text):
        return "not done yet"
