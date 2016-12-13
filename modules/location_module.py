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
        # with open("peoplelist.csv") as peoplelist:
        #     for line in peoplelist:
        #         if any(line.find(s) >= 0 for s in last_name_message):
        #             # office_number = line.split(", ")[2].split("-")
        #             # self.location_str = "building {}, room {}".format(office_number[0], office_number[1])
        #             # office_number = line.split(', ')[2]
        #             # if office_number == 0:
        #             #     return "he has no office or desk"
        #             # else:
        #             self.location_str = line
        #             self.location_str = last_name_message
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if last_name_message in line:
                    building_number = line.split(", ")[2]
                    self.location_str = "{}: {}".format(building_number.split("-")[0], building_number.split("-")[1])

# TODO add more keywords and create a csv with building and there numbers so it can tell the user the name/ they can
# put the name in and still get the map up
