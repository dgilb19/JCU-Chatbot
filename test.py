word_list = ()

with open("peoplelist.csv") as peoplelist:
    for line in peoplelist:
        word_list += tuple(line.split(", ")[0])

Userinput = str.lower(raw_input("Tell me about your day: "))

if any(Userinput.find(s) >= 0 for s in word_list):
    print("Quit Cursing!")

else:
    print("That sounds great!")
