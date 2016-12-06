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
                        self.location_str = "I know you are asking where something is, but I'm not that smart yet!!"

    # def location_passer_name(self, message_text):
    #     with open("buildinglist") as buildinglist:
    #         for line in buildinglist:
    #             if message_text in line:
    #                 building_number = line.title().split(", ")[1]
    #                 self.location_str = "Are you looking for this building? \nhttps://maps.jcu.edu.au/campus/townsville/?location={}".format(
    #                     building_number)


# TODO add more keywords and create a csv with building and there numbers so it can tell the user the name/ they can
# put the name in and still get the map up
