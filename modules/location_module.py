import re


class LocationIndex:
    def __init__(self, location_str):
        self.location_str = location_str

    def __str__(self):
        return "{}".format(self.location_str)

    def location_passer(self, message_text):
        if re.match(r'.*map', message_text, re.I):
            self.location_str = "Here's a map! https://maps.jcu.edu.au/campus/townsville/"

        elif re.match(r'.*[0-354]', message_text, re.I):
            message_text_number = re.findall('\d+', message_text)
            message_text_number = ("".join(message_text_number))
            self.location_str = "Are you looking for this building? \nhttps://maps.jcu.edu.au/campus/townsville/?location={}".format(message_text_number)

        elif re.match(r'.*pool|swim|swimming', message_text, re.I):
            self.location_str = "Are you looking for the pool man?\nhttps://maps.jcu.edu.au/campus/townsville/?location=241"

        else:
            with open("buildinglist.csv") as buildinglist:
                for line in buildinglist:
                    if message_text in line[0]:
                        building_number = line.title().split(", ")[1]
                        self.location_str = "Are you looking for this building? \nhttps://maps.jcu.edu.au/campus/townsville/?location={}".format(building_number)
                    else:
                        self.location_str = "idk what you are saying"

    def location_name_passer(self, message_text):
        with open("buildinglist.csv") as buildinglist:
            for line in buildinglist:
                if message_text in line.split(", ")[1]:
                    self.location_str = "are you looking for building {}?".format(line.title().split(", ")[0])

    def office_passer(self, last_name_message):
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if last_name_message in line:
                    if line.split(', ')[2] == '0\n':
                        self.location_str = "{} does not have an office".format(line.split(', ')[0])
                        # TODO fix this its so close^^^^^^
                    else:
                        building_number = line.split(", ")[2]
                        # building_number_final = "{}: {}".format(building_number.split("-")[0], building_number.split("-")[1])
                        building_number_final = "{}".format(building_number.split("-")[0])
                        self.location_str = building_number_final
            else:
                self.location_str = "im not sure who you are talking about 2"

                        #"""gets the last name entered and and gets email based of that"""

    def office_passer_new(self, last_name_message):
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if last_name_message in line:
                    line = line.split(", ")[2]
                    self.location_str = "{}: {}".format(line.split("-")[0], line.split("-")[1])
            else:
                self.location_str = "im not sure who you are talking about"

    def office_passer_with_name(self, name):
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if name in line:
                    # line = line.split(", ")[2]
                    # self.location_str = "{} : {}".format(line.split("-")[0], line.split("-")[1])
                    self.location_str = line.split(', ')[2]

# TODO add more keywords and create a csv with building and there numbers so it can tell the user the name/ they can
# put the name in and still get the map up
