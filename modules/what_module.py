import re


class WhatIndex:
    def __init__(self, what_str):
        self.what_str = what_str

    def __str__(self):
        return "{}".format(self.what_str)

    """gets the last name entered and and gets email based of that"""
    def email_passer(self, last_name_message):
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if last_name_message in line:
                    self.what_str = line.split(", ")[1]

    def email_passer_with_name(self, name):
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if name in line:
                    # self.what_str = "???"
                    self.what_str = line.split(", ")[1]
            else:
                self.what_str = "im not sure who you are talking about"
