final_text = ''

with open("buildinglist.csv") as text:
    for line in text:
        final_text += "{}".format(line.lower())

print final_text
