import re


class WhatIndex:
    def __init__(self, what_str):
        self.what_str = what_str

    def __str__(self):
        return "{}".format(self.what_str)

    def what_passer(self, last_name_used):
        # test = str(last_name_used)
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if "jerry" in line:
                    self.what_str = line.split(", ")[1]
