word_list = ("curse", 'cursing')

with open("peoplelist.csv") as peoplelist:
    for line in peoplelist:
        line = line.split(", ")[0]
        word_list += tuple(line.split(", "))
        line = line.split(" ")
        word_list += tuple(line)


Userinput = "jerry"

if any(Userinput.find(s) >= 0 for s in word_list):
    print("Quit Cursing!")
    print(word_list)

else:
    print("That sounds great!")
    print(word_list)
