class TimetableIndex:
    def __init__(self, timetable_str):
        self.timetable_str = timetable_str

    def __str__(self):
        return "{}".format(self.timetable_str)

    def timetable_passer(self, message_text):
        return "not done yet"
# TODO this is for a later date, make it know what time it is and give an appropriate response to questions such as
        # whens my next class, whens maths class next, how much time do i have until exam